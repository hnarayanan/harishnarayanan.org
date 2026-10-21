#!/bin/sh
# SPDX-FileCopyrightText: The Asahi Linux Contributors
# SPDX-FileCopyrightText: 2026 Harish Narayanan
# SPDX-License-Identifier: MIT
# Adapted from Asahi's scripts/bootstrap-prod.sh.
# The release builder puts the archive URL and checksum in this template.

# Do not execute a partially downloaded script.
if true; then
    set -eu
    export PATH=/usr/bin:/bin:/usr/sbin:/sbin
    export LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    if [ "$(uname -s)" != Darwin ]; then
        echo 'Start Hello Guix from macOS on the Mac you want to install.' >&2
        exit 1
    fi
    if ! arch -arm64 /usr/bin/true; then
        echo 'Hello Guix requires an Apple Silicon Mac.' >&2
        exit 1
    fi
    minimum_macos=26
    macos_version=$(sw_vers -productVersion)
    if ! [ "${macos_version%%.*}" -ge "$minimum_macos" ]; then
        printf 'This installer requires macOS %s or later.\n' "$minimum_macos" >&2
        exit 1
    fi
    action=install
    case "$*" in
        '') ;;
        --check) action=check ;;
        *) echo 'Usage: sh SCRIPT [--check]' >&2; exit 1 ;;
    esac
    if [ "$action" = install ]; then
        # curl | sh supplies the script on stdin. Give the installer the
        # user's terminal for its questions and administrator password.
        exec </dev/tty >/dev/tty 2>/dev/tty
    fi

    archive_url=https://github.com/hnarayanan/hello-guix/releases/download/v0.1/hello-guix-0.1.tar.gz
    archive_sha256=5f57b2887458f57e2bfc054a36d2261b846f30336d5a7ae8acf01c152323ff4b
    archive_kib=937998
    work_kib=1576742
    umask 077
    work=$(mktemp -d "${TMPDIR:-/tmp}/hello-guix.XXXXXX")
    partial=
    trap 'rm -rf "$work"; if [ -n "$partial" ]; then rm -f "$partial"; fi' 0
    trap 'exit 1' HUP INT TERM

    # Reuse the download for checks, installation, and retries.
    # The checksum identifies the required archive, regardless of its age.
    cache="$HOME/Library/Caches/Hello Guix"
    mkdir -p "$cache"
    archive="$cache/$archive_sha256.tar.gz"
    verified() {
        test -f "$1" && ! test -L "$1" &&
            printf '%s  %s\n' "$archive_sha256" "$1" | shasum -a 256 -c - >/dev/null 2>&1
    }
    printf '\nHello, Guix.\n'
    download_kib=$archive_kib
    if verified "$archive"; then download_kib=0; fi
    required_kib=$((download_kib + work_kib))
    # TMPDIR and the cache can be on different filesystems.
    # Require space for both download and extraction at each location.
    for directory in "$cache" "$work"; do
        if ! [ "$(df -Pk "$directory" | awk 'END {print $4}')" -ge "$required_kib" ]; then
            printf 'Hello Guix needs about %s MiB free in %s.\n' "$(((required_kib + 1023) / 1024))" "$directory" >&2
            exit 1
        fi
    done
    if [ "$download_kib" -eq 0 ]; then
        printf 'Using the verified installer download.\n'
    else
        printf 'Downloading the installer...\n'
        partial=$(mktemp "$cache/.download-XXXXXX")
        curl -fSL --proto '=https' \
            --output "$partial" "$archive_url"
        verified "$partial" || { echo 'Installer checksum mismatch.' >&2; exit 1; }
        mv -f "$partial" "$archive"
        partial=
    fi
    # Extract upstream ._* files as ordinary files, not as macOS metadata.
    tar --options '!mac-ext' -xzpf "$archive" -C "$work"
    caffeinate -dis /bin/bash "$work/hello-guix/install.sh" "$action"
fi

---
date: 2012-03-05
title: A command-line interface for Spotify on a Mac
short_title: Shpotify
thumbnail: /images/projects/shpotify.png
description: A command-line interface for Spotify on a Mac.
category: software
exterior_link: https://github.com/hnarayanan/shpotify/
start_date: 2012
end_date:
featured: true
---

Our media centre machine at home is an aging Mac with only one open
port: SSH. Since it was getting annoying to have to walk up to it
every time we wanted to control Spotify, I wrote [a simple Bash/Apple
script](https://github.com/hnarayanan/shpotify/) that allows us to
remotely control the program from other machines around the house (via
SSH).

With it, we can now do this:

<pre>megatr0n$ spotify
------------------------------------
A command-line interface for Spotify
------------------------------------
Usage: spotify &#60;option&#62;

Options:
 status   = Shows Spotify's status, current track details.
 play     = Start playing Spotify.
 pause    = Pause Spotify.
 next     = Go to the next track.
 prev     = Go to the previous track.
 vol up   = Increase Spotify's volume by 10%
 vol down = Increase Spotify's volume by 10%
 vol #    = Set Spotify's volume to # [0-100]
 quit     = Quit Spotify.

megatr0n$ spotify play
Playing Spotify.

megatr0n$ spotify status
Spotify is currently playing.
Artist: Kanye West
Album: Late Registration
Track: Gold Digger

megatr0n$ spotify vol up
Changing Spotify volume level.

megatr0n$ spotify pause
Pausing Spotify.

megatr0n$ spotify status
Spotify is currently paused.

megatr0n$ spotify play
Playing Spotify.

megatr0n$ spotify prev
Going to previous track.

megatr0n$ spotify status
Spotify is currently playing.
Artist: Cream
Album: Disreali Gears
Track: Tales Of Brave Ulysses

megatr0n$ spotify quit
Quitting Spotify.</pre>

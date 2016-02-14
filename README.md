# Harish Narayanan’s website

This repository contains the source code, assets and setup scripts for
my personal website: [harishnarayanan.org](https://harishnarayanan.org).
The site is generated using [Hugo](https://gohugo.io/) and its content
is mostly written in [Markdown](https://daringfireball.net/projects/markdown/).
The Linux server that’s hosting the site is setup using
[Ansible](http://www.ansible.com).

Be wary of cloning this code any time soon since this is a rapidly
evolving work in progress.

(c) Harish Narayanan 2016 **All Rights Reserved**.

## How to use this repository

The very first thing you ought to do is to get a copy of this
repository and move into it as the working directory.

````
git clone git@github.com:hnarayanan/harishnarayanan.org.git
cd harishnarayanan.org
````

This will take a while since this site contains a lot of large static
assets. In order to host a copy of the site, you need to do a couple
of things:

### Setup a web server to host the site

1. Go to your favourite cloud provider (I use [Digital
   Ocean](https://m.do.co/c/e3559ea013de)) and provision a virtual
   machine running [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/).

2. Make sure you can `ssh` to this virtual machine. Edit
   `config/servers/personal-site` to reflect the domain name (or IP)
   and `ssh` user name. Also update `domain_name` in
   `/config/site.yml` to point to your new server’s domain name.

3. Install [Ansible](http://www.ansible.com) on your local development
   machine.

4. Run the configuration script to setup the web server and other bits
   and bobs (like the firewall) on the virtual machine.

   ````
   cd config
   ansible-playbook site.yml -i servers/personal-site
   ````

### Build and upload the site to the web server

1. Install [hugo](https://gohugo.io) on your local development
   machine. Let’s assume it lives somewhere in `$PATH`.

2. Generate the site.

   ````
   $PATH/hugo --buildDrafts

   ````

3. Copy the generated files to the web server.

    ````
    rsync -aPvhe ssh --delete public/ ubuntu@harishnarayanan.org:/home/ubuntu/harishnarayanan.org
    ````

    Edit the domain name and virtual machine `ssh` user as needed.

## Everyday development

For day-to-day development and content writing, you can run `hugo`
locally to serve drafts of the site. This is an excellent way to work
as Hugo refreshes in the browser as you save files.


````
$PATH/hugo server --buildDrafts --watch
````

When you’re happy with your progess, you can build and publish the
site just as before.

## Checking links

This is just a command I find handy to reduce the instances of broken
links.

````
wget --spider -o wget.log -e robots=off -w 1 -r -p https://harishnarayanan.org/
````

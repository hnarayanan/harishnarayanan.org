# Harish Narayanan’s website

This repository contains the source code, assets and setup scripts for
my personal website: [harishnarayanan.org](https://harishnarayanan.org).
The site is generated using [Hugo](https://gohugo.io/), and its content
is mostly written in [Markdown](https://daringfireball.net/projects/markdown/).
The site is hosted using a Linux server that’s setup using
[Ansible](http://www.ansible.com).

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
   machine running [Ubuntu 16.04
   LTS](http://releases.ubuntu.com/16.04/) to act as your new server.

2. Make sure you can SSH to this server. Edit
   `config/servers/personal-site` to reflect the domain name (or IP
   address) of the server, as well as the SSH username you use to
   access it. Also update `domain_name` in `/config/site.yml` to point
   to your new server’s domain name.

3. Install [Ansible](http://www.ansible.com) on your local development
   machine.

4. Run the configuration script to setup the web server and other bits
   and bobs (like the firewall) on the virtual machine.

   ````
   cd config
   ansible-playbook site.yml -i servers/personal-site
   ````

### Build and upload the site to the web server

1. Install [Hugo](https://gohugo.io) on your local development
   machine.

2. Update `Makefile` to reflect your local path to the `hugo`
   executable, as well as your server’s SSH username and domain name.

3. Generate the site.

   ````
   make
   ````

4. Copy the generated files to the web server.

   ````
   make publish
   ````

## Everyday development

For day-to-day development and content writing, you can run `hugo`
locally to serve drafts of the site. This is an excellent way to work
as Hugo refreshes in the browser as you save files. Just make sure
`hugo` is in your path and run:

````
$PATH/hugo server --watch
````

When you’re happy with your progess, you can build and publish the
site just as before.

## Checking links

This is just a command I find handy to reduce the instances of broken
links. It spiders through the site and outputs the status of links to
`wget.log`.

````
make checklinks
````

## Copyright and license

Copyright (c) 2016 [Harish Narayanan](https://harishnarayanan.org).

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

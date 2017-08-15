---
title: "Right-Click Image Uploads for Static Sites on macOS"
date: 2017-08-13T22:28:31Z
url: /blog/2017/08/13/right-click-image-uploads-for-static-sites-on-macos/
categories: []
---

Quick and dirty post on something cool I've just learned.

While putting together this blog, I've wanted an easy way to add an image to a post. I've long appreciated Dropbox's auto-uploading screenshots, and wanted something that easy. Here's how I did it:

### Create an "upload" script

("Upload" is a bit of a misnomer here -- the actual uploading is done by the blog's rsync deploy. Still, it's the closest match to how I thought of it when writing the script.)

Normally I'd write this in bash/zsh, but in this case I think Python's easier to read:

<script src="https://gist.github.com/ternus/c83cff50b0bfb75cc695d2365fa893ed.js"></script>

### Create an Automator service to call that upload script

1. Open up Automator (should be built-in on macOS)
2. New -> Service
3. Library -> Actions -> Utilities -> Run Shell Script

![Screenshot_2017-08-13_22.32.28.png](/uploads/2017/8/13/Screenshot_2017-08-13_22.32.28.png)

4. Service receives selected *files or folders* in *Finder.app*
5. Pass input *as arguments* (don't forget this!)
6. Create a shell script that calls your `upload.py` file

![Screenshot_2017-08-13_22.38.53.png](/uploads/2017/8/13/Screenshot_2017-08-13_22.38.53.png)

7. Save it as something like "Upload to Blog Static Dir"
8. Done! Right-click an image -> Services -> Upload to Blog Static Dir and watch the magic happen!

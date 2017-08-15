#!/usr/bin/env python

import os
import sys
import shutil
import datetime
import pyperclip
import subprocess

clipboard_copy = pyperclip.clipboards.init_osx_clipboard()[0]

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

if len(sys.argv) == 1:
    print "Usage: %s file.jpg [file.jpg ...]" % sys.argv[0]
    sys.exit(1)

copy_str = ""

for fname in sys.argv[1:]:
    
    bname = os.path.basename(fname)

    if not os.path.exists(fname):
        sys.stderr.write("File not found: %s\n" % fname)
        sys.exit(1)
    if not os.path.exists(STATIC_DIR):
        sys.stderr.write("Couldn't find static dir %s\n" % STATIC_DIR)
        sys.exit(1)

    today = datetime.date.today()
    upload_path = os.path.join("uploads",
                            str(today.year),
                            str(today.month),
                            str(today.day))

    full_upload_path = os.path.join(STATIC_DIR, upload_path)

    if not os.path.exists(full_upload_path):
        os.makedirs(full_upload_path)
    
    bname = bname.replace(' ', '_')

    target = os.path.join(full_upload_path, bname)

    if not os.path.exists(target):
        shutil.copy(fname, target) 

    ext = target.split('.')[-1]
    target_sm = target[:-(len(ext) + 1)] + "-640x480." + ext

    bname_sm = os.path.basename(target_sm)

    if ext in ['jpg', 'jpeg', 'png']:
        print target, target_sm
        subprocess.check_call(["convert", "-resize", "640x480>", target, target_sm]) 

    copy_str += "<div class='image'><a href='/%s/%s'><img src='/%s/%s' class='uploaded-img' /></a></div>\n" % \
            (upload_path, bname, upload_path, bname_sm)

    print "Copied %s to %s" % (fname, target)

clipboard_copy(copy_str)

print "Done and copied to clipboard."

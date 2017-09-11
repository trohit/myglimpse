#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
"""
Created on Sun Aug 27 10:35:43 2017
@author: guess
"""
import flask
import subprocess
import commands
import urllib
import re
import cgi

hdr1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
'''
hdr2 = '''
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--
    <link rel="stylesheet" href="/highlight/default.min.css">
    <script src="/highlight/highlight.min.js"></script>
    -->
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.6/styles/default.min.css">
    <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.6/highlight.min.js"></script>
    <script>
        hljs.initHighlightingOnLoad();
    </script>
</head>
<body>
<pre>
<code class="cpp">
'''
ftr = '''
</code>
</pre>
</body>
</html>
'''

app = flask.Flask(__name__)
@app.route("/<path:myfile>")
def showmyfile(myfile):
    if myfile == "favicon.ico":
        return ""
    print("cat " + myfile)
    process = subprocess.Popen(['cat', myfile], stdout = subprocess.PIPE)
    out, err = process.communicate()
    out = cgi.escape(out)

    title = "<title>" + myfile[-25:] + "</title>"
    hdr = hdr1 + title + hdr2
    page = hdr + out + ftr
    #print(out)
    return(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

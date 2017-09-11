#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# very quick rough draft hack - will refactor later
"""
Created on Sun Aug 27 10:35:43 2017

@author: rohit
"""

import flask
import subprocess
import commands
import urllib
import re

app = flask.Flask(__name__)

def _get_list_from_lines(res):
    lines = re.split('\n', res)
    #for i in range(len(lines)):
    #    lines[i] = re.split('\s+', lines[i])
    return lines

def _get_filename(line):
    parts = line.split(':')
    abspath = parts[0]
    relpath = abspath.split('/', 3)[3]
    return relpath


@app.route("/<string:gstr>")
def glimpse(gstr):
    count = 0
    #gstr = urllib.unquote_plus(gstr)
    prefix = "You queried for :<br><b>" + gstr + "<b><br>"

    out ='<html>\n' + prefix
    #res = os.system("ls -l " + gstr)
    cmd = '/usr/local/bin/glimpse -y ' + ' "' + gstr + '"'
    print(cmd)
    res = commands.getoutput(cmd)
    res = _get_list_from_lines(res)
    #print(type(res))
    for l in res:
        if len(l) == 0:
            print("skipping this one")
            return("No results.")
            continue
        print("\nprocessing line "+ str(count)+ str(len(l)))
        count += 1
        #out = out + str(count) + ":" + l + "<br>"
        print("finding relpath for:[" + l +"]")
        #out = out + '\n' + str(count) + " <a href='http://10.207.85.26:3000/" + _get_filename(l) + "'>" + (l) + "</a><br>"
        out = out + '\n' + str(count) + " <a href='http://10.207.85.26:5000/" + _get_filename(l) + "'>" + (l) + "</a><br>"
    out = out + "<br>" + '</html>'

    return(out)

#    for line in res:
#        out += "<a href='http://10.207.85.26:3000/" + line + "'>" + out + "</a>"
    return(res + "lines:" + str(count))
#    print(out)
#    return(str(out) + str(err))
    #return "will glimpse for [" + str(gstr) + "]"

@app.route("/show/<path:file>")
def showfile(file):
    print("cat " + file)
    process = subprocess.Popen(['cat', ' ', file], stdout = subprocess.PIPE)
    out, err = process.communicate()
    print(out)
    return(out)



@app.route("/")
def main():
    str= '<html><form method="get" action="data"> Enter search string - case insensitive search:<br><input type="text" name="q"><br></form>'
    return str

@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    gstr = flask.request.args.get('q')
    count = 0
    #gstr = urllib.unquote_plus(gstr)
    prefix = "You queried for :<br><b>" + gstr + "<b><br>"

    out ='<html>\n' + prefix
    #res = os.system("ls -l " + gstr)
    cmd = '/usr/local/bin/glimpse -y -i ' + ' "' + gstr + '"'
    print(cmd)
    res = commands.getoutput(cmd)
    res = _get_list_from_lines(res)
    #print(type(res))
    for l in res:
        if len(l) == 0:
            print("skipping this one")
            return("No results.")
            continue
        print("\nprocessing line "+ str(count)+ str(len(l)))
        count += 1
        #out = out + str(count) + ":" + l + "<br>"
        print("finding relpath for:[" + l +"]")
        #out = out + '\n' + str(count) + " <a href='http://10.207.85.26:3000/" + _get_filename(l) + "'>" + (l) + "</a><br>"
        out = out + '\n' + str(count) + " <a href='http://10.207.85.26:5000/" + _get_filename(l) + "'>" + (l) + "</a><br>"
    out = out + "<br>" + '</html>'

    return(out)

#    for line in res:
#        out += "<a href='http://10.207.85.26:3000/" + line + "'>" + out + "</a>"
    return(res + "lines:" + str(count))

def showhifile():
    return

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

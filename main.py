#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

#enable debugging
import cgitb
import os
import time
cgitb.enable()

def main():
    template = "view/template.inc"
    sitename = "http://collegestarterkit.net/"
    tpl = "".join(open(template,'r').readlines())
    print 'Content-type: text/html; charset=utf-8\n\n' + tpl

if __name__ == '__main__':
    main()

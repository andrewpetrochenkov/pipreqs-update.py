#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
import requests

def getnames(path):
    names = []
    for l in open(path).read().splitlines():
        name = l.split("#")[0].split(">")[0].split("<")[0].split("=")[0]
        if name:
            names.append(name)
    return names

def get_latest_version(name):
    url = "https://pypi.org/pypi/%s/json" % name
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    return data["info"]["version"]

@public.add
def update(path):
    """update pip requirements file with latest versions"""
    lines = []
    for name in getnames(path):
        version = get_latest_version(name)
        lines.append('%s==%s' % (name,version))
    open(path,"w").write("\n".join(lines))

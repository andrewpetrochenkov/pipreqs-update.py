#!/usr/bin/env python
"""update pip requirements file with latest versions"""
# -*- coding: utf-8 -*-
import click
import sys
import pipreqs_update

MODULE_NAME = "pipreqs_update"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path' % MODULE_NAME


@click.command()
@click.argument('path')
def _cli(path):
    pipreqs_update.update(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)

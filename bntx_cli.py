#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python version: sanity check
minimum = 3.4
import sys
import os.path
import argparse
import glob

import bntx as BNTX
import globals

from PIL import Image

parser = argparse.ArgumentParser(description='CLI for BNTX Editor', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i', '--input', help='input .bntx', type=argparse.FileType('r'), nargs='+', default=['*.bntx'])
parser.add_argument('-o', '--outdir', help='output folder', default='out')

args = parser.parse_args()
files = []
for fn in args.input:
    files.extend(glob.glob(fn))
args.input = files

if not os.path.isdir(args.outdir):
    os.mkdir(args.outdir)

for fn in args.input:
    x = BNTX.File()
    x.readFromFile(fn)
    x.extract(0, os.path.dirname(os.path.abspath(fn)), 0)
    for fn in glob.glob('*.dds'):
        os.rename(fn, 'out/' + fn)
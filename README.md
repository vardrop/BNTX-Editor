# BNTX-Editor [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) ![GitHub](https://img.shields.io/github/license/aboood40091/BNTX-Editor.svg)
A tool for editing Binary Resources Texture (BNTX) files

The tool is pretty straight forward, just run it and you will hopefully know what to do.

## Installation

```shell
$ pip3 install --user -r requirements.txt
```

## Start

```shell
$ python3 bntx_editor.py
```

## Error codes:
* 1: Invalid byte order mark (BOM)
* 2: Invalid file header
* 3: Unsupported target
* 4: Invalid section header / section missing

# Credits:
* AboodXD: Making this thing
* libtxc_dxtn: BC1/2/3 decompressors
* gdkchan: Helping with the relocation table
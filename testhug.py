#! /usr/bin/env python3

import hug
import webcolors

@hug.get()
def hextoname(hex: hug.types.text):
    return webcolors.hex_to_name("#" + hex)

@hug.get()
def nametohex(name: hug.types.text):
    return webcolors.name_to_hex(name)

#! /usr/bin/env python3

import ctypes
import pathlib

if __name__ == "__main__":
    libname = pathlib.Path().absolute() / "libcmult.dylib"
    c_lib = ctypes.CDLL(libname)
    
    c_lib.cmult.restype = ctypes.c_float
    x, y = 6, 2.3
    answer = c_lib.cmult(x, ctypes.c_float(y))
    print(f"In Python main: x: {x}, y: {y}, answer = {answer:.1f}")

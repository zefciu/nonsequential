#!/bin/sh
python3.4 setup.py build
cp build/lib.linux-x86_64-3.4/cperfect.cpython-34m.so cperfect.so

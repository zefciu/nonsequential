from distutils.core import setup, Extension

ccollatz = Extension('ccollatz', sources = ['ccollatz.c'])

setup (name = 'Collatz',
       version = '1.0',
       description = 'Collatz package',
       ext_modules = [ccollatz]
)


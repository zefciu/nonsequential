from distutils.core import setup, Extension

cperfect = Extension('cperfect', sources = ['cperfect.c'])

setup (name = 'Perfect',
       version = '1.0',
       description = 'Cperfect package',
       ext_modules = [cperfect]
)


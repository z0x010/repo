#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(
    pypi_name='tldextract',
    depends=['python-idna'],
  )

def post_build():
  pypi_post_build()
  update_aur_repo()

if __name__ == '__main__':
  single_main()

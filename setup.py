#!/usr/bin/env python

from distutils.core import setup
from kott import __kott_author__
from kott import __kott_url__
from kott import __kott_name__
from kott import __kott_version__
from kott import __kott_packages__
from kott import __kott_description__
from kott import __kott_author_email__
from kott import __kott_package_dir__

setup(name=__kott_name__,
      version=__kott_version__,
      description=__kott_description__,
      author=__kott_author__,
      author_email=__kott_author_email__,
      url=__kott_url__,
      # package_dir=__kott_package_dir__,
      packages=__kott_packages__,)

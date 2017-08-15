# pylint: disable-msg=F0401

import os
import sys
from setuptools import setup, find_packages

here = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(here,
                                                 'src',
                                                 'oottadao',
                                                 'util')))

import releaseinfo
version = releaseinfo.__version__

setup(name='oottadao.util',
      version=version,
      description="various utility routines",
      long_description="""\
""",
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='http://oottadao.org',
      license='Apache License, Version 2.0',
      namespace_packages=["oottadao"],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      package_data={
          'oottadao.util.test': ['src/doubler.py']
      },
      test_suite='nose.collector',
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pycrypto==2.3',
          'pyparsing',
          'Traits==4.3.0',
          #'PyYAML==3.09',
      ],
      entry_points="""
      [console_scripts]
      xyplot=oottadao.util.casedb:cmdlineXYplot
      plotgraph=oottadao.util.graphplot:main
      dotgraph=oottadao.util.dotgraph:main
      add_reqs=oottadao.util.addreqs:add_reqs
      mkpseudo=oottadao.util.mkpseudo:mkpseudo
      envdump=oottadao.util.envirodump:envdump
      pstadump=oottadao.util.dep:main
      update_libpath=oottadao.util.lib:update_libpath
      combine_paths=oottadao.util.lib:combine_paths
      """
      )
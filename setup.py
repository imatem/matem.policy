from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='matem.policy',
      version=version,
      description="Policy package for the InfoMatem project",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Gildardo Bautista',
      author_email='gil@matem.unam.mx',
      url='http://matem.unam.mx',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['matem'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.Collage',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

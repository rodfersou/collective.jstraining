from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(name='collective.jstraining',
      version=version,
      description="Package to be used as a base for js traing",
      long_description="%s\n%s" % (
          open("README.rst").read(),
          open("CHANGES.rst").read()
      ),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='javascript plone',
      author='Nathan Van Gheem',
      author_email='vangheem@gmail.com',
      url='https://github.com/collective/collective.jstraining',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools'
      ],
      extras_require={
          'test': [
              'plone.app.testing'
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

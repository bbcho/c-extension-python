from setuptools import setup, Extension
import setuptools

setup(name = "main",
      # packages=setuptools.find_packages("src"),
      # package_dir={"": "src"},
      version = "0.1",
      # packages=['risktools'],
      # ext_package = 'main',
      ext_modules = [Extension("main", ["sub.c"])]
      );

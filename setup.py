from setuptools import setup
from setuptools.extension import Extension

extensions = [
    Extension(
    name="sub", 
    sources=["main/sub.c"])
]

setup(name='main',
      # packages=['main'],
      ext_package='main',
      ext_modules = extensions,
)
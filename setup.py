from setuptools import setup, find_packages

setup(name="falcon",
      version="1.0",
      packages=find_packages(),
      install_requires=["pycryptodome", "numpy"])

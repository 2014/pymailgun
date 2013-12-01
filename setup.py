#!/usr/bin/python
#-*-coding: ;utf8-*-

from setuptools import setup, find_packages

setup(
    name="pymailgun",
    version="0.0.1",
    author="fatelei",
    author_email="fatelei@gmail.com",
    description="mailgun sdk for python",
    packages=find_packages('mailgun'),
    install_requires=["requests"],
    packages=["mailgun", "mailgun.data"]
)

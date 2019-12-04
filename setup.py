# !/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="segment-config-api",
    packages=find_packages(),
    version="0.0.1",
    description="A Python Wrapper for Segment's Config API",
    author="Michael Erasmus",
    license="MIT",
    author_email="michael@buffer.com",
    url="https://github.com/bufferapp/segment-config-api",
    keywords=["segment"],
    install_requires=["requests"],
)
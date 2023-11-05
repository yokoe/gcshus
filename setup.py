# Author: yokoe <kreuz45@kreuz45.com>
# Copyright (c) 2023- yokoe
# Licence: MIT

from setuptools import setup

DESCRIPTION = "gcshus: GCS helper utils."
NAME = "gcshus"
AUTHOR = "yokoe"
AUTHOR_EMAIL = "kreuz45@kreuz45.com"
URL = "https://github.com/yokoe/gcshus"
LICENSE = "MIT"
DOWNLOAD_URL = URL
VERSION = "0.0.4"
PYTHON_REQUIRES = ">=3.6"
INSTALL_REQUIRES = [
    "google-cloud-storage>=2.7.0",
]
PACKAGES = ["gcshus"]
KEYWORDS = "gcs"
CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6",
]
with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES,
)

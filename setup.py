from setuptools import setup, find_packages
import os

long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="price-parser-reworkd",
    version="0.2.0",
    author="Mohamed Khalil",
    author_email="mkhalil@reworkd.ai",
    description="A simple price parser for extracting currency and value from strings (currently used as a Pydantic datatype only).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohamedmamdouh22/price-parser.git",
    packages=find_packages(),
    install_requires=["pydantic", "pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

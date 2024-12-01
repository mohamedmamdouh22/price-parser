from setuptools import setup, find_packages

setup(
    name="price-parser",
    version="0.1.0",
    author="Mohamed Khalil",
    author_email="mkhalil@reworkd.ai",
    description="A simple price parser for extracting currency and value from strings(currently used as pydantic datatype only).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mohamedmamdouh22/price_parser",
    packages=find_packages(),
    install_requires=["pydantic", "pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

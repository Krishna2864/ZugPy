from setuptools import setup, find_packages

setup(
    name="zugpy",
    version="0.1.0",
    description="A Python library for creating and validating ZUGFeRD invoices.",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=[
        "pikepdf",
        "reportlab",
        "lxml",
        "xmlschema"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

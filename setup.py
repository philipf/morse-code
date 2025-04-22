from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="morse-code",
    version="0.1.0",
    author="Philip Fourie",
    description="A Python application to convert English text to Morse code and vice versa",
    url="https://github.com/philipf/morse-code",
    packages=find_packages(include=["."]),
    py_modules=["encode", "decode", "morse_utils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    tests_require=["pytest>=7.4.0"],
) 
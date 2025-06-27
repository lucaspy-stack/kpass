from setuptools import setup, find_packages

setup(
    name="kpass",
    version="0.1.1",
    author="Lucas Paulino Da Silva",
    author_email="lucas.workps@gmail.com",
    description="kpass is a simple password generator based on name, age and birthdate.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lucaspy-stack/kpass",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "rich"
    ],
)

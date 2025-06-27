from setuptools import setup, find_packages

setup(
    name="Passrord_Generator",
    version="0.1.0",
    author="Lucas Paulino Da Silva",
    author_email="lucas.workps@gmailcom",
    description="The **passwords_generator** is a simple module that, given a full name, age, and birth date, generates password combinations between 6 and 18 characters",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lucaspy-stack/passwords_generator",
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

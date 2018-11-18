# coding:utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xshell",
    version="1.4",
    author="@neoctobers",
    author_email="neoctobers@gmail.com",
    description="Run `xshell.embed()`, you can do anything, in the Interactive Console.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neoctobers/xshell",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)

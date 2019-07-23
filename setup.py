import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybitcore",
    version="0.1",
    author="Wei Wang",
    author_email="tianshanghong@outlook.com",
    description="Python3 wrapper for the Bitcore API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tianshanghong/pybitcore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
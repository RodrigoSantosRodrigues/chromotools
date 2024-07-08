from setuptools import find_packages, setup

setup(
    name="chromotools",
    version="0.1.3Beta",
    packages=find_packages(),
    install_requires=[],
    author="Rodrigo J. R Santos",
    author_email="contato@daftar.digital",
    description="Toolkit for chromosome segmentation, designed for advanced genetic analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/daftar/chromotools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

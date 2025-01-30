from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="BAGEL2",
    version="v2.0-115",
    packages=find_packages(),
    py_modules=["BAGEL"],
    install_requires=required,
    entry_points={
        "console_scripts": [
            "bagel=BAGEL:bagel",
        ],
    },
    author="Traver Hart",
    author_email="traver@hart-lab.org",
    description="The Bayesian Analysis of Gene Essentiality 2 (BAGEL2) is a robust gene essentiality identifier from CRISPR-cas9 genome wide pooled library screen data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hart-lab/BAGEL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)

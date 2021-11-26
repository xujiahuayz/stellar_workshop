from setuptools import setup, find_packages

setup(
    name="stellar",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "requests",
        "matplotlib",
        "stellar-sdk",
    ],
    extras_require={"dev": ["pylint", "black"]},
)

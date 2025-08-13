from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-HOTEL-RESERVATION-PREDICTION",
    version="0.0.1",
    author="Avishek",
    packages=find_packages(),
    install_requires = requirements,
)
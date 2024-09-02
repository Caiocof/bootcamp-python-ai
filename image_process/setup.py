from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    page_description = fh.read()

with open("requirements.tst") as fh:
    requirements = fh.read().splitlines()

setup(
    name="image_process",
    version="0.0.1",
    author="caiocof",
    author_email="caiooliveira3652@outlook.com",
    description="Module to processa images",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Caiocof/bootcamp-python-ai/tree/refact-bank",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)

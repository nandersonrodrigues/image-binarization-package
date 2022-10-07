from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_binarization",
    version="0.0.1",
    author="Nanderson Rodrigues",
    author_email="nandersondsr@gmaillcom",
    description="Image binarization project example",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nandersonrodrigues/image-binarization-package"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
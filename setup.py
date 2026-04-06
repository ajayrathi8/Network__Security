from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="NetworkSecurity",
    version="0.1.0",
    description="A network security analysis project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ajay Rathi",
    author_email="rathiajay08@gmail.com",
    url="https://github.com/ajayrathi8/NetworkSecurity",
    packages=find_packages(include=["NetworkSecurity", "NetworkSecurity.*"]),
    install_requires=[
        "python-dotenv",
        "pandas",
        "numpy",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)

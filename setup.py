import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='useful_classes',
    version='0.1.4',
    author="Benzi",
    author_email="BarakBenZion@gmail.com",
    description="A bundle of useful python classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BarakBenzi/useful_classes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "useful_classes"},
    packages=setuptools.find_packages(where="useful_classes"),
    python_requires=">=3.6",
)

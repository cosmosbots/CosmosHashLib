import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CosmosHashLib",
    version="0.0.6",
    author="Cosmos Bots",
    author_email="contact@cosmosbots.com",
    description="A simple hashing wrapper with support for salts and peppers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vihangatheturtle/CosmosHashLib",
    project_urls={
        "Bug Tracker": "https://github.com/vihangatheturtle/CosmosHashLib/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
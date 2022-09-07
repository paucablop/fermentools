import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fermentools",
    version_config=True,
    setup_requires=["setuptools-git-versioning"],
    author="Pau Cabaneros",
    author_email="pau.cabaneros@gmail.com",
    description="Package to teach chemometrics in the context of fermentation processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paucablop/fermentools",
    project_urls={
        "Bug Tracker": "https://github.com/paucablop/fermentools/issues/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.10",
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "mbpls",
        "scipy",
        "scikit-learn",
    ],
    include_package_data=True,
    package_data={'': ['datasets/data/*.csv']}
)

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='pydevquotes',
    version='0.1',
    author="Pankaj Kumar",
    author_email="pankaj08072000@gmail.com",
    description="A 'Quotes for Developers' scraping package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shankusu993/pydevquotes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)

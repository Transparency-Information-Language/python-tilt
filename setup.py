import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tilt",
    version="0.0.4",
    author="Elias Grünewald",
    author_email="gruenewald@tu-berlin.de",
    description="A python language binding for the Transparency Information Language and Toolkit (TILT)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Transparency-Information-Language/python-tilt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

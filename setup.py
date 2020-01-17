import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='challenge-calc',
    version='0.1.0',
    author="mconsta000",
    packages=setuptools.find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
)
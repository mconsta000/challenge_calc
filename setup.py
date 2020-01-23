import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    include_package_data=True,
    name='challenge-calc',
    version='0.1.0',
    author="mconsta000",
    author_email="",
    packages=setuptools.find_packages(),
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mconsta000/challenge_calc",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
)
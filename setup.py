import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

setuptools.setup(
    name="textSummarizer",  # The name of your package
    version=__version__,
    author="Jothsna Praveena", 
    author_email="jothsnapraveena1421@gmail.com",
    description="A package for performing text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jothsnapraveena/Text-Summarization",
    packages=setuptools.find_packages(),  # This will find and include your package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Assuming MIT license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

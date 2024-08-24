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
    long_description_content="text/markdown",
    url="https://github.com/jothsnapraveena/Text-Summarization",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),  # This will find and include your package
    
)

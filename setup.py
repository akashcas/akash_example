import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="akash-example",
    version="0.1",
    author="akash",
    author_email="akashmagrawal@gmail.com",
    description="A function that returns 'hello world'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akashcas/akash_example",
    packages=setuptools.find_packages()
)
from setuptools import setup

with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    url="https://github.com/Lilly81324/ft_package",
    author="sikunne",
    author_email="sikunne@42.fr",
    license='MIT',
    python_requires='>=3.8',
    packages=["ft_package"],
    long_description=description,
    long_description_content_type="text/markdown",
    install_requires=[]
)

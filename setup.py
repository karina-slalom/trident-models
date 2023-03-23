import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="trident-models-package",
    version="0.0.1",
    author="Karina",
    author_email="karina.ge@slalom.com",
    packages=["trident-models-package"],
    description="ORM Mmodels",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
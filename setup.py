from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-list-with-loader",
    version="0.1.3",
    author="Firdaus A. Indradhirmaya",
    author_email="fai14@pitt.edu",
    description="A streamlist component that allows you to have a liist with loading status",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=["streamlit>=1.2", "jinja2"],
)

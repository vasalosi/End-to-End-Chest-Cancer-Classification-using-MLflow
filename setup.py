import setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-Chest-Cancer-Classification-using-MLflow"
AUTHOR_USER_NAME = "vasalosi"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "vasalosi@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=REPO_NAME,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    proect_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
       package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
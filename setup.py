from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer_Project"
AUTHOR_USER_NAME = "sonalben-ops"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sonal.itit29@gmail.com"



def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer NPL Application",
    long_description=long_description,
    long_description_content="text/markdown",
    #url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    # project_urls={
    #     "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    # },
    #package_dir={"","src"},
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
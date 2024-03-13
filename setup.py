from setuptools import find_packages,setup
from typing import List


def get_requirements() -> List[str]:
    requirements_list = []
    with open('requirements.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('-e'):  # Exclude lines starting with -e
                requirements_list.append(line)
    return requirements_list

setup(
    name='sensor',
    version='0.01',
    author='Shamsher',
    author_email='mohammad.sahmsher682@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    dependency_links=['-e .'],  # Add the local editable installation
)




'''
This function will return list of all requirements

from setuptools import find_packages, setup

def get_requirements() -> list[str]:
    requirements_list = []
    with open('requirements.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                requirements_list.append(line)
    return requirements_list

setup(
    name='sensor',
    version='0.01',
    author='Shamsher',
    author_email='mohammad.sahmsher682@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)


'''





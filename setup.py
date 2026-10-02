from setuptools import setup ,find_packages
from typing import List 

def get_requirements()->List[str]:
    requirements_list : list[str] = []
    try:
        with open("requirements.txt",'r') as file:
            lines = file.readlines()
            for line in lines :
                requirements = line.strip()
            if requirements and requirements != "e .":
                requirements_list.append(requirements)
        
    except FileNotFoundError:
        print("requirements.txt file  not found")

setup(
    name="NetworkSecurity",
    author="Sai Varhdan Reddy",
    author_email="sai.gsvr@gmail.com",
    install_requires=get_requirements(),
    packages=find_packages()
)


# ways to create virtual environment

# python -m venv .venv

# conda create -n myvenv

# virtualenv .venv 

# uv venv 

# poetry env (pip  install poetry)

# pipenv install


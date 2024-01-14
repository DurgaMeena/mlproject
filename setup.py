from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e . '
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        for line in file_obj:
            new_line = line.replace("\n","")
            if new_line == HYPEN_E_DOT:
                continue
            requirements.append(new_line)

        return requirements
            
      

setup(
name='mlproject',
version='0.0.1',
author='Krish',
author_email='krishnaik06@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)


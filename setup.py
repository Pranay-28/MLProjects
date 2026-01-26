# from setuptools import setup, find_packages
# from Typing import List

# HYPEN_DOT_E ="-e ."
# def get_requirements(file_path: str) -> List[str]:
#     requirements =[]
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace("\n", "") for req in requirements]

#         if HYPEN_DOT_E in requirements:
#             requirements.remove(HYPEN_DOT_E)

#     return requirements


# setup(
#     name="mlpropjects",
#     version="0.0.1",
#     author="Pranay",
#     author_email="pranaybambole11@gmail.com",
#     packages=find_packages(),
#     install_requires=get_reuirements("requirements.txt")

# )

from setuptools import setup, find_packages

setup(
    name="mlprojects",
    version="0.0.1",
    author="Pranay",
    author_email="pranaybambole11@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)

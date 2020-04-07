from setuptools import setup,find_packages

setup(
    name = 'src',
    version = '1.0.0',
    install_reqiures=['pytest'],
    packages = find_packages(), install_requires=['sqlalchemy', 'sqlalchemy_mptt', 'treelib', 'jsonpickle', 'flask',
                                                  'pytest']
)
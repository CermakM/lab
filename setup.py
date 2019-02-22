import os

from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def get_install_requires():
    with open('requirements.txt', 'r') as requirements_file:
        # TODO: respect hashes in requirements.txt file
        res = requirements_file.readlines()
        return [req.split(' ', maxsplit=1)[0] for req in res if req]


def get_version():
    with open(os.path.join('thoth', 'lab', '__init__.py')) as f:
        content = f.readlines()

    for line in content:
        if line.startswith('__version__ ='):
            # dirty, remove trailing and leading chars
            return line.split(' = ')[1][1:-2]
    raise ValueError("No version identifier found")


setup(
    name='thoth-lab',
    version=get_version(),
    description='Code for Thoth experiments in Jupyter notebooks.',
    long_description=Path('README.rst').read_text(),
    author='Fridolin Pokorny',
    author_email='fridolin@redhat.com',
    license='GPLv3+',
    packages=[
        'thoth.{subpackage}'.format(subpackage=p)
        for p in find_packages('thoth/')
    ],
    zip_safe=False,
    install_requires=get_install_requires()
)

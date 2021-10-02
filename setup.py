from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='cloudphoto',
    version='0.0.1',
    author='Aliev Emin',
    packages=['cloudphoto'],
    package_data={},
    install_requires=required,
    entry_points={
        'console_scripts': ['cloudphoto = cloudphoto.cli:start']
    }
)

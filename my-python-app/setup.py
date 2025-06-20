from setuptools import setup, find_packages

setup(
    name='my-python-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'my-python-app = app.main:main'
        ]
    },
)

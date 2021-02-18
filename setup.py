from setuptools import setup, find_packages

setup(
    name='vaultr',
    version='0.1.0',
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        vaultr=src.commands:actions
    '''
)
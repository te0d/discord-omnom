from setuptools import find_packages, setup

setup(
    name='discord-omnom',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'BTrees',
        'discord.py',
        'Flask',
        'transaction',
        'zeo',
        'ZODB',
    ],
)


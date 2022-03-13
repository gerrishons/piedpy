from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="piedpy",
    install_requires=[
        "quo >= 2022.3",
        'cryptography >= 1.0.0',
        'PyMySQL >= 0.9.2',
        'sqlparse>=0.3.0,<0.5.0',
        'configobj >= 5.0.5',
        'cli_helpers[styles] >= 2.0.1',
        'pyaes >= 1.6.1',
    ],
    package_data={'piedpy': ['piedpyrc']},
 #   scripts= ['timeanddate'],
    extras_require={
        'ssh':  ['paramiko'],
    },
)

from setuptools import setup
setup(
    name = 'CLIApplication',
    version = '0.1.0',
    packages = ['rndmcli'],
    entry_points = {
        'console_scripts': [
            'rndmcli = rndmcli.__main__:main'
        ]
    })

from setuptools import setup

setup(
    name='sophon',
    version='1.0',
    packages=['sophon'],
    url='https://github.com/monitor1379/sophon',
    license='MIT',
    author='monitor1379',
    author_email='yy4f5da2@hotmail.com',
    description='This is Description',
    entry_points={
        'console_scripts': [
            'sophon = sophon.__main__:cli',
        ],
    },
    requires=['inspect', 'shutil', 'yaml', 'click'],
    platforms=['Windows', 'Linux', 'Mac']
)

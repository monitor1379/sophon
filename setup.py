from setuptools import setup

setup(
    name='sophon',
    version='0.1.0',
    packages=['sophon', 'sophon.cmd', 'sophon.test'],
    include_package_data=True,
    url='https://github.com/monitor1379/sophon',
    license='MIT',
    author='monitor1379',
    author_email='yy4f5da2@hotmail.com',
    description='Automatic API Markdown Documentation Generation for Python',
    entry_points={
        'console_scripts': [
            'sophon = sophon.__main__:cli',
        ],
    },
    install_requires=['pyyaml', 'click'],
    platforms=['Windows', 'Linux', 'Mac']
)

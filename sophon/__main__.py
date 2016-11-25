# encoding: utf-8

import click
import logging

from sophon import __version__
from sophon.cmd import new, build


def create_log():
    log = logging.getLogger("sophon")
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s][%(levelname)s]: %(message)s ")
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    log.addHandler(ch)


create_log()

help_build = 'Build API documentations.'
help_new = 'Create a configuration file.'
help_config_file = 'Specify a configuration file.'
default_config_file = 'sophon.yml'


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__, '-v', '--version')
def cli():
    """
    Sophon - Automatic API Markdown Documentation Generation for Python
    """


@cli.command('build', help=help_build)
@click.option('-f', '--config-file', type=click.File('r'), default=default_config_file, help=help_config_file)
def run_sophon_build(config_file):
    log = logging.getLogger(__name__)
    log.info('Specify config_file:{}'.format(config_file.name))
    config_file.close()
    build.build_from_yaml(config_file.name)


@cli.command('new', help=help_new)
def run_sophon_new():
    log = logging.getLogger(__name__)
    log.info('Creating Sophon configuration file: sophon.yml...')
    new.new_yaml()
    log.info('Create done!')


if __name__ == '__main__':
    cli()

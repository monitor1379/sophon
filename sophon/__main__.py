# encoding: utf-8

import click

from sophon import __version__
from sophon.build import build_from_yaml
from sophon.log import ConsoleLogger

help_build = 'Build API documents.'
help_config_file = 'Specify a configuration file.'
default_config_file = 'sophon.yml'


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__, '-v', '--version')
def cli():
    """
    Sophon - Auto documentation tool for Python project
    """


@cli.command('build', help=help_build)
@click.option('-f', '--config-file', type=click.File('r'), default=default_config_file, help=help_config_file)
def build(config_file):
    logger = ConsoleLogger()
    logger.info('specify config_file:' % config_file.name)
    config_file.close()
    build_from_yaml(config_file.name)


if __name__ == '__main__':
    cli()

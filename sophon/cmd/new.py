# encoding: utf-8

import os
import shutil

config_example_fn = '{}/{}'.format(os.path.dirname(__file__), 'sophon.example.yml')


def new_yaml():
    config_fn = '{}/{}'.format(os.getcwd(), 'sophon.yml')
    shutil.copy(config_example_fn, config_fn)


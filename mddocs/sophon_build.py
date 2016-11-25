# encoding: utf-8

from sophon.cmd.build import build_from_yaml

def run():
    build_from_yaml('sophon.yml')


if __name__ == '__main__':
    run()
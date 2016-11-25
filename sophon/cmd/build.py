# encoding: utf-8
from __future__ import print_function

import logging
import os
import shutil
import sys

import yaml

from sophon import parsers
from sophon.utils import import_from_name

default_build_dir = 'api'
log = logging.getLogger("sophon")


def _to_abs_path(directory, path):
    """Convert relative path to absolute path"""
    if os.path.isabs(path):
        return os.path.normpath(path)
    else:
        return os.path.normpath(directory + os.sep + path)


def build_from_yaml(config_fn):
    """Build documentations of python project given the configuration filename.

    # Argument
        config_fn: `str`. Sophon configuration filename.

    # Return
        `None`
    """
    config_fn = os.path.abspath(config_fn)
    # ==========================================================================
    # load configuration from sophon.yml
    log.info('Loading configuration file: {}'.format(config_fn))
    with open(config_fn, 'r') as f:
        config = yaml.load(f)
    pages = config.get('pages')  # necessary
    if not pages:
        log.warn('Sophon: There is no pages to build.')
        return

    repo_url = config.get('repo_url')
    branch = config.get('branch', 'master')
    log.info('Using repo_url: {}'.format(repo_url))
    log.info('Using branch: {}'.format(branch))

    style = config.get('style', 'sophon')
    parser = parsers.get(style)
    if not parser:
        message = 'Invalid style:{}, only support Sophon/reStructuredText/Google/NumPy style!'.format(style)
        raise KeyError(message)

    # ==========================================================================
    # process build_dir and template_dir
    code_dir = config.get('code_dir')
    template_dir = config.get('template_dir')
    build_dir = config.get('build_dir')
    conf_dir = os.path.dirname(config_fn)

    # for supporting absolute path of sophon.yml
    if code_dir:
        code_dir = _to_abs_path(conf_dir, code_dir)
    else:
        code_dir = conf_dir
    sys.path.insert(0, code_dir)

    if template_dir:
        template_dir = _to_abs_path(conf_dir, template_dir)

    if build_dir:
        build_dir = _to_abs_path(conf_dir, build_dir)
    else:
        build_dir = conf_dir + os.sep + default_build_dir

    log.info('Using code dir: {}'.format(code_dir))
    log.info('Using template dir: {}'.format(template_dir))
    log.info('Using build dir: {}'.format(build_dir))

    # ==========================================================================
    # clean build_dir
    log.info('Creating build_dir...')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        os.makedirs(build_dir)
    log.info('Create done')

    # check template_dir
    if template_dir and not os.path.exists(template_dir):
        message = 'template_dir is not exist! {}'.format(template_dir)
        raise Exception(message)
    # ==========================================================================
    # for every page
    for page in pages:
        # =======================================================
        # get build filename and template filename
        build_fn = page['page']  # necessary
        template_fn = page.get('template')  # not necessary
        log.info('===========================')
        log.info('Building file: {}'.format(build_fn))
        log.info('Using template file: {}'.format(template_fn))
        # =======================================================
        # check template file
        if template_fn:
            if template_dir:
                template_fn = os.path.normpath(template_dir + os.sep + template_fn)
                if not os.path.exists(template_fn):
                    message = 'Template file does not exist! template file: {}'.format(template_fn)
                    raise Exception(message)
            else:
                raise Exception('Can not find template_dir!')
        # =======================================================
        # check build file
        build_fn = os.path.normpath(build_dir + os.sep + build_fn)
        build_fn_dir = os.path.dirname(build_fn)
        if not os.path.exists(build_fn_dir):
            os.makedirs(build_fn_dir)
        # =======================================================
        # get template markdown from template_file
        if template_fn:
            with open(template_fn) as temp_f:
                build_md = temp_f.read()
        else:
            log.info('No template to load')
            build_md = ''
        # pre-write
        log.info('Creating page...')

        with open(build_fn, 'w') as f:
            f.write(build_md)
        log.info('Create done')
        # =======================================================
        # start generating docstring
        tags = page.get('tags')
        if not tags:
            log.warn('No tags in page:{}'.format(build_fn))
            continue

        with open(build_fn, 'r') as f:
            build_file_doc = f.read()
        # =======================================================
        for tag in tags:
            # ===============================
            tag_name = tag.get('tag')
            tag_doc = ''
            log.info('-------------------------')
            log.info('Current tag: %s' % tag_name)
            log.info('generateing doc...')

            # ===============================
            # generate markdown from classes
            classes = tag.get('classes')
            if classes:
                for class_name in classes:
                    class_ = import_from_name(class_name)
                    docstring = parser.parse_from_class(class_, repo_url=repo_url, branch=branch)
                    tag_doc += docstring

            classes_with_methods = tag.get('classes_with_methods')
            if classes_with_methods:
                for class_name in classes_with_methods:
                    class_ = import_from_name(class_name)
                    docstring = parser.parse_from_class_with_methods(class_, repo_url=repo_url, branch=branch)
                    tag_doc += docstring

            # ===============================
            # generate markdown from functions
            functions = tag.get('functions')
            if functions:
                for function_name in functions:
                    function = import_from_name(function_name)
                    docstring = parser.parse_from_function(function, repo_url=repo_url, branch=branch)
                    tag_doc += docstring

            # ===============================
            # replace {{tag}} by tag_doc
            if tag_name:
                if tag_name not in build_file_doc:
                    message = '{} is not in file {}. markdown doc will append to the file.'.format(tag_name,
                                                                                                   page['page'])
                    log.warn(message)
                    build_file_doc += tag_doc
                else:
                    log.info('Replacing tag: %s' % tag_name)
                    build_file_doc = build_file_doc.replace('{{%s}}' % tag_name, tag_doc)
                    log.info('Replace done')
            else:
                message = '{} has a tag without name. markdown doc will append to the file.'.format(page['page'])
                log.warn(message)
                build_file_doc += tag_doc

        # =======================================================
        # write markdown doc to build_file
        log.info('Writing doc to page...')
        with open(build_fn, 'w') as f:
            f.write(build_file_doc)
        log.info('Write done')

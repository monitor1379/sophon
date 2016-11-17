# encoding: utf-8

import inspect
import os
import re
import shutil
import warnings

import yaml


def extract_function_signature(function, ismethod=False):
    argspec = inspect.getargspec(function)
    defaults = argspec.defaults
    keywords = argspec.keywords

    # if function is a method of a class, then
    # remove the first argument 'self'
    if ismethod:
        args = argspec.args[1:]
    else:
        args = argspec.args

    # if function has arguments with default value
    if defaults:
        kwargs = zip(args[-len(defaults):], defaults)
        args = args[:-len(defaults)]
    else:
        kwargs = []

    signature = function.__module__ + '.' + function.__name__
    signature += '('
    # add args
    for arg in args:
        signature += str(arg) + ', '
    # add kwargs
    for arg, val in kwargs:
        if type(val) == str:
            val = "'" + val + "'"
        signature += str(arg) + '=' + str(val) + ', '
    # add keywords
    if keywords:
        signature += '**' + keywords + ', '
    # remove ', '
    if args or kwargs or keywords:
        signature = signature[:-2]
    signature += ')'
    return signature


def extract_class_signature(clazz):
    try:
        signature = extract_function_signature(clazz.__init__, ismethod=True)
        signature = signature.replace('__init__', clazz.__name__)
    except:
        # in case the class inherits from object and
        # does not define '__init__' function
        signature = clazz.__module__ + '.' + clazz.__name__ + '()'
    return signature


def extract_function_docstring(function):
    docstring = inspect.getdoc(function)
    if not docstring:
        return ''

    # replace '# something'  to '**something**'
    docstring = re.sub(r'\n[ ]*# (.*)\n',
                       r'\n**\1**\n\n',
                       docstring)

    # replace 'something: desc' to '- **something**: desc'
    docstring = re.sub(r'\n[ ]*(\S*):(.*)\n',
                       r'\n- **\1**:\2\n',
                       docstring)

    '''
    in case:
        ```
        **Arguments**

        - **foo**: here is tag1.
            and here is tag2.
        - **bar**: tag3 here too.
        ```
    the follow code is meant to indent "and here is tag2" to left.
    '''
    docstring = re.sub(r'(\n- \*\*.*\*\*.*\n)    (.*)\n',
                       r'\1\2\n\n',
                       docstring)

    # left indentation
    docstring = docstring.replace('\n    ', '\n')
    return docstring


def extract_class_docstring(clazz):
    return extract_function_docstring(inspect.getdoc(clazz))


def code_snippet(snippet):
    result = '```python\n'
    result += snippet + '\n'
    result += '```\n'
    return result


def import_from_name(name):
    names = name.split('.')
    mod = __import__(names[0])
    for i in range(1, len(names)):
        mod = getattr(mod, names[i])
    return mod


def generate_function_markdown(function):
    signature = extract_function_signature(function, inspect.ismethod(function))
    docstring = extract_function_docstring(function)
    md = ''
    md += '# ' + function.__name__ + '\n\n'
    md += code_snippet(signature) + '\n'
    md += docstring
    md += '---\n\n'
    return md


def generate_class_markdown(clazz):
    signature = extract_class_signature(clazz)
    docstring = extract_class_docstring(clazz)
    md = ''
    md += '# ' + clazz.__name__ + '\n\n'
    md += code_snippet(signature) + '\n'
    md += docstring
    md += '---\n\n'
    return md


def sophon_build():
    conf_fn = 'sophon.yml'
    conf_fn = os.path.abspath(conf_fn)

    # ==========================================================================
    # load configuration from sophon.yaml
    print 'loading configuration file:', conf_fn
    yml = yaml.load(open(conf_fn, 'r'))
    pages = yml.get('pages')  # necessary
    if not pages:
        print 'Sophon: There is no pages to build.'
        return

    # ==========================================================================
    # process build_dir and template_dir
    template_dir = yml.get('template_dir')
    build_dir = yml.get('build_dir')
    conf_dir = os.path.dirname(conf_fn)

    # for supporting absoluted path of sophon.yaml
    if template_dir:
        if os.path.isabs(template_dir):
            template_dir = os.path.normpath(template_dir)
        else:
            template_dir = os.path.normpath(conf_dir + os.sep + template_dir)

    if build_dir:
        if os.path.isabs(build_dir):
            build_dir = os.path.normpath(build_dir)
        else:
            build_dir = os.path.normpath(conf_dir + os.sep + build_dir)
    else:
        build_dir = conf_dir + os.sep + 'build'

    print 'template dir:', template_dir
    print 'build dir:   ', build_dir

    # ==========================================================================
    # clean build_dir
    print 'creating build_dir...'
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        os.makedirs(build_dir)
    print 'creat done'

    # check template_dir
    if template_dir and not os.path.exists(template_dir):
        raise Exception('Error: template_dir:{} is not exist!'.format(template_dir))
    # ==========================================================================
    # for every page
    for page in pages:
        # =======================================================
        # get build filename and template filename
        build_fn = page['page']  # necessary
        template_fn = page.get('template')  # not necessary
        print '==========================='
        print 'building file:', build_fn
        print 'template file:', template_fn
        # =======================================================
        # check template file
        if template_fn:
            if template_dir:
                template_fn = os.path.normpath(template_dir + os.sep + template_fn)
                if not os.path.exists(template_fn):
                    raise Exception('Error: template file:{} does not exist!'.format(template_fn))
            else:
                raise Exception('Error: can not find template_dir!')
        # =======================================================
        # check build file
        build_fn = os.path.normpath(build_dir + os.sep + build_fn)
        build_fn_dir = os.path.dirname(build_fn)
        if not os.path.exists(build_fn_dir):
            os.makedirs(build_fn_dir)
        # =======================================================
        # get template markdown from template_file
        if template_fn:
            print 'loading template...'
            build_md = open(template_fn).read()
            print 'load done'
        else:
            print 'no template to load'
            build_md = ''
        # pre-write
        print 'creating page...'
        open(build_fn, 'w').write(build_md)
        print 'create done'
        # =======================================================
        # start generating docstring
        tags = page.get('tags')
        if not tags:
            print 'no tags'
            continue

        build_file_doc = open(build_fn, 'r').read()
        # =======================================================
        # for every tag
        for tag in tags:
            # ===============================
            tag_name = tag.get('tag')
            tag_doc = ''
            print 'generating tag:', tag_name
            # ===============================
            # generate markdown from functions
            functions = tag.get('functions')
            if functions:
                for function_name in functions:
                    function = import_from_name(function_name)
                    docstring = generate_function_markdown(function)
                    tag_doc += docstring
            # ===============================
            # generate markdown from classes
            classes = tag.get('classes')
            if classes:
                for class_name in classes:
                    clazz = import_from_name(class_name)
                    docstring = generate_class_markdown(clazz)
                    tag_doc += docstring

            # ===============================
            # replace {{tag}} by tag_doc
            if tag_name:
                if tag_name not in build_file_doc:
                    message = tag_name + ' is not in file:' + page['page'] \
                              + '. markdown doc will append to the file'
                    warnings.warn(message)
                    build_file_doc += tag_doc
                else:
                    build_file_doc = build_file_doc.replace('{{' + tag_name + '}}', tag_doc)
            else:
                message = page['page'] + ' has a tag without name. ' + \
                          'markdown doc will append to the file'
                warnings.warn(message)
                build_file_doc += tag_doc
        # =======================================================
        # write markdown doc to build_file
        print 'writting doc to file...'
        open(build_fn, 'w').write(build_file_doc)
        print 'write done'

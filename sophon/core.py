# encoding: utf-8
from __future__ import print_function

import inspect
import os
import re
import shutil
import sys

import yaml

__all__ = [
    'code_snippet',
    'extract_function_signature',
    'extract_class_signature',
    'extract_function_docstring',
    'extract_class_docstring',
    'generate_function_markdown',
    'generate_class_markdown',
    'import_from_name',
    'sophon_build',
    'get_repo_link',
]


def extract_function_signature(function, ismethod=False):
    """given a function, return the signature string of function.

    # Arguments
        function: function object.
        ismethod: boolean. represents that the function is a method of a class or not.
            Note that if a "method" of class is static, then it is a `function` instead of `method`.
            The simplest way to distinguish `function` and `method` is to see if there is a argument
            named `self` in the arguments list of the function.

    # Returns
        a string signature of function.

    # Examples
        assume that there are some functions in a module named `mod`:
        ```python
        # mod.py
        import sophon

        def foo1():
            pass

        def foo2(a, b='b', c=None, **kwargs):
            pass

        print sophon.extract_function_signature(foo1)
        # print "mod.foo1()" to the console

        print sophon.extract_function_signature(foo2)
        # print "mod.foo2(a, b='b', c=None, **kwargs)" to the console
        ```

        now we add a class named `bar` to mod.py:
        ```python
        # mod.py
        import sophon

        class bar(object):

            def baz1(self):
                pass

            def baz2(self, a, b='b', c=None, **kwargs):
                pass

            @staticmethod
            def baz3(a, b='b', c=None):
                pass


        print sophon.extract_function_signature(bar.baz1, ismethod=True)
        # print "mod.bar.baz1()" to the console

        print sophon.extract_function_signature(bar.baz2, ismethod=True)
        # print "mod.bar.baz2(a, b='b', c=None, **kwargs)" to the console

        print sophon.extract_function_signature(bar.baz3, ismethod=False)
        # print "mod.bar.baz3(a, b='b', c=None, **kwargs)" to the console


        ```


    """
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
    """given a class, return the signature string of function `class.__init__`.

    # Arguments
        clazz: class object.

    # Returns
        a string signature of function `class.__init__`.

    # Examples
        ```python
        # mod.py
        import sophon

        class foo(object):
            def __init__(self):
                pass

        class bar(object):
            def __init__(self, a, b='b', c=None, **kwargs):
                pass

        print extract_class_signature(foo)
        # print "mod.foo()" to the console

        print extract_class_signature(bar)
        # print "mod.bar(a, b='b', c=None, **kwargs)" to the console

        ```
    """
    try:
        signature = extract_function_signature(clazz.__init__, ismethod=True)
        signature = signature.replace('__init__', clazz.__name__)
    except:
        # in case the class inherits from object and
        # does not define '__init__' function
        signature = clazz.__module__ + '.' + clazz.__name__ + '()'
    return signature


def extract_function_docstring(function):
    """extract the docstring of function and change it into standard markdown style.

    # Arguments
        function: function object.

    # Returns
        str type. markdown docstring of the function.
    """
    docstring = inspect.getdoc(function)
    if not docstring:
        return ''

    # replace '# something'  to '**something**'
    docstring = re.sub(r'\n# (.*)\n',
                       r'\n**\1**\n\n',
                       docstring)

    # replace 'something: desc' to '- **something**: desc'
    docstring = re.sub(r'\n    (\S*):(.*)',
                       r'\n\n- **\1**:\2',
                       docstring)

    # left indentation
    docstring = docstring.replace('\n    ', '\n')
    return docstring


def extract_class_docstring(clazz):
    """extract the docstring of class and change it into standard markdown style.

    # Arguments
        clazz: class object.

    # Returns
        str type. markdown docstring of the class.

    # Note
        only extract the docstring of class, exclude member of the given class.

    # Examples
        ```python
        import sophon

        class foo(object):
            '''This is docstring of foo
            '''

            def bar(self):
                '''This is docstring of bar
                '''
                pass

        print sophon.extract_class_docstring(foo)
        # print "This is docstring of foo" to the console

        ```
    """
    return extract_function_docstring(clazz)


def code_snippet(snippet):
    """change a string-typed code snippet into markdown-style code fence.

    # Arguments
        snippet: str type. a code snippet.

    # Returns
        str type. markdown-style code fence.

    """
    result = '```python\n'
    result += snippet + '\n'
    result += '```\n'
    return result


def import_from_name(name):
    """import module from string.

    # Arguments
        name: str. such as `foo`, `foo.someclass` or `foo.somefunction`.

    # Returns
        the module object, it could be module-typed, class-typed or function-typed.
    """
    names = name.split('.')
    mod = __import__(names[0])
    for i in range(1, len(names)):
        mod = getattr(mod, names[i])
    return mod


def get_repo_link(obj, repo_url, branch='master'):
    """Get the definition position of obj in source file, then link it to GitHub repo.

    # Arguments
        obj: function object or class object.
        repo_url: such as `https://github.com/yourusername/yourrepo`
        branch: repo branch.

    # Returns
        Return the hyperlink of obj.
    """
    module_name = obj.__module__
    path = module_name.replace('.', '/')
    path += '.py'
    line = inspect.getsourcelines(obj)[-1]
    link = repo_url + '/blob/' + branch + '/' + path + '#L' + str(line)
    return '[[source]](' + link + ')'


def generate_function_markdown(function, repo_url, branch):
    """given a function object, generate markdown documents.

    # Arguments
        function: function object.
        repo_url: such as `https://github.com/yourusername/yourrepo`
        branch: repo branch.

    # Returns
        str type. markdown documents of the function.

    """
    signature = extract_function_signature(function, inspect.ismethod(function))
    signature = signature.replace(function.__module__ + '.', '')
    docstring = extract_function_docstring(function)
    md = ''
    if repo_url:
        md += '<span style="float:right;">' + get_repo_link(function, repo_url, branch) + '</span>' + '\n\n'
    md += '## ' + function.__name__ + '\n\n'
    md += code_snippet(signature) + '\n'
    md += docstring + '\n\n'
    md += '---\n\n'
    return md


def generate_class_markdown(clazz, repo_url=None, branch='master'):
    """given a class object, generate markdown documents.

    # Arguments
        clazz: class object.
        repo_url: such as `https://github.com/yourusername/yourrepo`
        branch: repo branch.

    # Returns
        str type. markdown documents of the class.

    """
    signature = extract_class_signature(clazz)
    docstring = extract_class_docstring(clazz)
    md = ''
    if repo_url:
        md += '<span style="float:right;">' + get_repo_link(clazz, repo_url, branch) + '</span>' + '\n\n'
    md += '## ' + clazz.__name__ + '\n\n'
    md += code_snippet(signature) + '\n'
    md += docstring + '\n\n'
    md += '---\n\n'
    return md


def sophon_build(config_fn):
    """build documents of python project given the configuration filename

    # Arguments
        config_fn: Sophon configuration filename.

    # Returns
        None
    """
    config_fn = os.path.abspath(config_fn)

    # ==========================================================================
    # load configuration from sophon.yml
    print('loading configuration file:', config_fn)
    yml = yaml.load(open(config_fn, 'r'))
    pages = yml.get('pages')  # necessary
    if not pages:
        print('Sophon: There is no pages to build.')
        return

    repo_url = yml.get('repo_url')
    branch = yml.get('branch', 'master')
    print('repo_url:', repo_url)
    print('branch:', branch)

    # ==========================================================================
    # process build_dir and template_dir
    code_dir = yml.get('code_dir')
    template_dir = yml.get('template_dir')
    build_dir = yml.get('build_dir')
    conf_dir = os.path.dirname(config_fn)

    # for supporting absoluted path of sophon.yml
    if code_dir:
        if os.path.isabs(code_dir):
            code_dir = os.path.normpath(code_dir)
        else:
            code_dir = os.path.normpath(conf_dir + os.sep + code_dir)
    else:
        code_dir = conf_dir

    sys.path.insert(0, code_dir)

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

    print('code dir:    ', code_dir)
    print('template dir:', template_dir)
    print('build dir:   ', build_dir)

    # ==========================================================================
    # clean build_dir
    print('creating build_dir...')
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        os.makedirs(build_dir)
    print('create done')

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
        print('===========================')
        print('building file:', build_fn)
        print('template file:', template_fn)
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
            print('loading template...')
            build_md = open(template_fn).read()
            print('load done')
        else:
            print('no template to load')
            build_md = ''
        # pre-write
        print('creating page...')
        open(build_fn, 'w').write(build_md)
        print('create done')
        # =======================================================
        # start generating docstring
        tags = page.get('tags')
        if not tags:
            print('no tags')
            continue

        build_file_doc = open(build_fn, 'r').read()
        # =======================================================
        # for every tag
        for tag in tags:
            # ===============================
            tag_name = tag.get('tag')
            tag_doc = ''
            print('-------------------------')
            print('current tag:', tag_name)
            print('generateing doc...')

            # ===============================
            # generate markdown from functions
            functions = tag.get('functions')
            if functions:
                for function_name in functions:
                    function = import_from_name(function_name)
                    docstring = generate_function_markdown(function, repo_url, branch)
                    tag_doc += docstring

            # ===============================
            # generate markdown from classes
            classes = tag.get('classes')
            if classes:
                for class_name in classes:
                    clazz = import_from_name(class_name)
                    docstring = generate_class_markdown(clazz, repo_url, branch)
                    tag_doc += docstring

            # ===============================
            # replace {{tag}} by tag_doc
            if tag_name:
                if tag_name not in build_file_doc:
                    message = tag_name + ' is not in file:' + page['page'] \
                              + '. markdown doc will append to the file'
                    print('warning:', message)
                    build_file_doc += tag_doc
                else:
                    print('replacing tag:', tag_name)
                    build_file_doc = build_file_doc.replace('{{' + tag_name + '}}', tag_doc)
                    print('replace done')
            else:
                message = page['page'] + ' has a tag without name. ' + \
                          'markdown doc will append to the file'
                print('warning:', message)
                build_file_doc += tag_doc

        # =======================================================
        # write markdown doc to build_file
        print('writing doc to file...')
        open(build_fn, 'w').write(build_file_doc)
        print('write done')

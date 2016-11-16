# encoding: utf-8

import inspect
import re


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
    md = []
    md.append('# ' + function.__name__ + '\n')
    md.append(code_snippet(signature))
    md.append(docstring)
    md.append('---\n')
    md = '\n'.join(md)
    return md


def generate_class_markdown(clazz):
    signature = extract_class_signature(clazz)
    docstring = extract_class_docstring(clazz)
    md = []
    md.append('# ' + clazz.__name__ + '\n')
    md.append(code_snippet(signature))
    md.append(docstring)
    md.append('---\n')
    md = '\n'.join(md)
    return md

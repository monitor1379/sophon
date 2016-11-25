# encoding: utf-8

import inspect


def extract_function_signature(function, ismethod=False):
    """Given a function, return the signature string of function.

    # Arguments
        function: `function`.
        ismethod: `boolean`. Represent that if the given function is a method of a class or not.
            Note that if a "method" of class is static, then it is a `function` instead of `method`.
            The simplest way to distinguish `function` and `method` is to see if there is a argument
            named `self` in the arguments list of the function.

    # Return
        `str`: A string signature of function.

    # Examples
        Assume that there are some functions in a module named `mod`:
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

        Now we add a class named `bar` to mod.py:
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
        signature = '{}.{}.{}'.format(function.__module__, function.im_class.__name__, function.__name__)
    else:
        args = argspec.args
        signature = function.__module__ + '.' + function.__name__

    # if function has arguments with default value
    if defaults:
        kwargs = zip(args[-len(defaults):], defaults)
        args = args[:-len(defaults)]
    else:
        kwargs = []
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
    """Given a class, return the signature string of function `class.__init__`.

    # Argument
        clazz: `class object`.

    # Return
        `str`: A string signature of function `class.__init__`.

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
        signature = signature.replace('.__init__', '')
    except:
        # in case the class inherits from object and
        # does not define '__init__' function
        signature = clazz.__module__ + '.' + clazz.__name__ + '()'
    return signature


def code_snippet(snippet):
    """Change a string-typed code snippet into Markdown-style code fence.

    # Argument
        snippet: `str`. A code snippet.

    # Return
        `str`: Markdown-style code fence.

    """
    return '```python\n{}\n```'.format(snippet)


def import_from_name(name):
    """Import module from string.

    # Argument
        name: `str`. Such as `foo`, `foo.someclass` or `foo.somefunction`.

    # Return
        `module`: It could be module-typed, class-typed or function-typed.
    """
    names = name.split('.')
    mod = __import__(names[0])
    for i in range(1, len(names)):
        mod = getattr(mod, names[i])
    return mod


def generate_repo_link(obj, repo_url, branch):
    """Get the definition position of obj in source file, then link it to GitHub repo.

    # Arguments
        obj: `function object` or `class object`.
        repo_url: `str`. such as `https://github.com/yourusername/yourrepo`
        branch: `str`. repo branch.

    # Return
        `str`: Return the hyperlink of obj.
    """
    module_name = obj.__module__
    path = module_name.replace('.', '/')
    path += '.py'
    line = inspect.getsourcelines(obj)[-1]
    link = '{}/blob/{}/{}#L{}'.format(repo_url, branch, path, str(line))
    md_link = '[[source]]({})'.format(link)
    return md_link

# Sophon

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L226)</span>

## code_snippet

```python
code_snippet(snippet)
```

Change a string-typed code snippet into markdown-style code fence.

**Arguments**

- **snippet**: `str`. a code snippet.

**Returns**

`str`. markdown-style code fence.

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L26)</span>

## extract_function_signature

```python
extract_function_signature(function, ismethod=False)
```

Given a function, return the signature string of function.

**Arguments**

- **function**: `function object`.
- **ismethod**: `boolean`. represents that the function is a method of a class or not.
    Note that if a "method" of class is static, then it is a `function` instead of `method`.
    The simplest way to distinguish `function` and `method` is to see if there is a argument
    named `self` in the arguments list of the function.

**Returns**

`str`. A string signature of function.

**Examples**

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

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L126)</span>

## extract_class_signature

```python
extract_class_signature(clazz)
```

Given a class, return the signature string of function `class.__init__`.

**Arguments**

- **clazz**: `class object`.

**Returns**

`str`. A string signature of function `class.__init__`.

**Examples**

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

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L165)</span>

## extract_function_docstring

```python
extract_function_docstring(function)
```

Extract the docstring of function and change it into standard markdown style.

**Arguments**

- **function**: `function object`.

**Returns**

`str`. markdown docstring of the function.

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L193)</span>

## extract_class_docstring

```python
extract_class_docstring(clazz)
```

Extract the docstring of class and change it into standard markdown style.

**Arguments**

- **clazz**: `class object`.

**Returns**

`str`. markdown docstring of the class.

**Note**

Only extract the docstring of class, excluding members of the given class.

**Examples**

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

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L277)</span>

## generate_function_markdown

```python
generate_function_markdown(function, repo_url, branch)
```

Given a function object, generate markdown documents.

**Arguments**

- **function**: `function object`.
- **repo_url**: `str`. such as `https://github.com/yourusername/yourrepo`
- **branch**: `str`. repo branch.

**Returns**

`str`. markdown documents of the function.

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L302)</span>

## generate_class_markdown

```python
generate_class_markdown(clazz, repo_url=None, branch='master')
```

Given a class object, generate markdown documents.

**Arguments**

- **clazz**: `class object`.
- **repo_url**: `str`. such as `https://github.com/yourusername/yourrepo`
- **branch**: `str`. repo branch.

**Returns**

`str`. markdown documents of the class.

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L242)</span>

## import_from_name

```python
import_from_name(name)
```

Import module from string.

**Arguments**

- **name**: `str`. such as `foo`, `foo.someclass` or `foo.somefunction`.

**Returns**

`module object`. it could be module-typed, class-typed or function-typed.

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/core.py#L326)</span>

## sophon_build

```python
sophon_build(config_fn)
```

Build documents of python project given the configuration filename

**Arguments**

- **config_fn**: `str`. Sophon configuration filename.

**Returns**

None

---


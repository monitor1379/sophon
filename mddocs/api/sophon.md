# sophon/core.py

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L6)</span>

## extract_function_signature

```python
sophon.utils.extract_function_signature()
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

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L106)</span>

## extract_class_signature

```python
sophon.utils.extract_class_signature()
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

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L145)</span>

## code_snippet

```python
sophon.utils.code_snippet()
```

Change a string-typed code snippet into markdown-style code fence.

**Arguments**

- **snippet**: `str`. a code snippet.

**Returns**

`str`. markdown-style code fence.

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L158)</span>

## import_from_name

```python
sophon.utils.import_from_name()
```

Import module from string.

**Arguments**

- **name**: `str`. such as `foo`, `foo.someclass` or `foo.somefunction`.

**Returns**

`module object`. it could be module-typed, class-typed or function-typed.

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L174)</span>

## generate_repo_link

```python
sophon.utils.generate_repo_link()
```

Get the definition position of obj in source file, then link it to GitHub repo.

**Arguments**

- **obj**: `function object` or `class object`.
- **repo_url**: `str`. such as `https://github.com/yourusername/yourrepo`
- **branch**: `str`. repo branch.

**Returns**

`str`. Return the hyperlink of obj.

---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L10)</span>

## Parser

```python
sophon.parsers.Parser()
```



---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L24)</span>

## SophonParser

```python
sophon.parsers.SophonParser()
```



---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L81)</span>

## ReStructuredTextParser

```python
sophon.parsers.ReStructuredTextParser()
```



---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L98)</span>

## GoogleDocParser

```python
sophon.parsers.GoogleDocParser()
```



---

<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L115)</span>

## NumPyDocParser

```python
sophon.parsers.NumPyDocParser()
```



---


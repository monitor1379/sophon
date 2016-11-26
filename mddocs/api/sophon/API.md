# API documentations of Sophon

This is some API documentations of Sophon.

# sophon/parsers.py



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L10)</span>

## Parser

```python
sophon.parsers.Parser()
```

Top level base class of parsers.


---



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L155)</span>

## ReStructuredTextParser

```python
sophon.parsers.ReStructuredTextParser()
```

Support soon.

---



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L178)</span>

## GoogleDocParser

```python
sophon.parsers.GoogleDocParser()
```

Support soon.

---



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L201)</span>

## NumPyDocParser

```python
sophon.parsers.NumPyDocParser()
```

Support soon.

---



## SophonParser

```python
sophon.parsers.SophonParser()
```

A docstring parser for parsing Sophon style docstring to Markdown.


---




<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L86)</span>

### SophonParser.parse_from_class

```python
sophon.parsers.SophonParser.parse_from_class(class_, **kwargs)
```

Extract docstring from class and parse it to Markdown text.

**Arguments**

- **class_**: `class`. A class with Sophon style docstring.
- ****kwargs**: `dict`.

**Return**

- **`str`**: Markdown text.

---




<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L116)</span>

### SophonParser.parse_from_class_with_methods

```python
sophon.parsers.SophonParser.parse_from_class_with_methods(class_, **kwargs)
```

Extract docstring from class and its public members, and parse it to Markdown text.

**Arguments**

- **class_**: `class`. A class with Sophon style docstring.
- ****kwargs**: `dict`.

**Return**

- **`str`**: Markdown text.

---




<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L37)</span>

### SophonParser.parse_from_docstring

```python
sophon.parsers.SophonParser.parse_from_docstring(docstring, **kwargs)
```

Parse Sophon style docstring to Markdown text.

**Arguments**

- **docstring**: `str`. Sophon style docstring.
- ****kwargs**: `dict`.

**Return**

- **`str`**: Markdown text.

---




<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/parsers.py#L56)</span>

### SophonParser.parse_from_function

```python
sophon.parsers.SophonParser.parse_from_function(function, **kwargs)
```

Extract docstring from function and parse it to Markdown text.

**Arguments**

- **function**: `function`. A function with Sophon style docstring.
- ****kwargs**: `dict`.

**Return**

- **`str`**: Markdown text.

---



# sophon/utils.py



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L6)</span>

## extract_function_signature

```python
sophon.utils.extract_function_signature(function, ismethod=False)
```

Given a function, return the signature string of function.

**Arguments**

- **function**: `function`.
- **ismethod**: `boolean`. Represent that if the given function is a method of a class or not.
    Note that if a "method" of class is static, then it is a `function` instead of `method`.
    The simplest way to distinguish `function` and `method` is to see if there is a argument
    named `self` in the arguments list of the function.

**Return**

- **`str`**: A string signature of function.

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

---



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L106)</span>

## extract_class_signature

```python
sophon.utils.extract_class_signature(clazz)
```

Given a class, return the signature string of function `class.__init__`.

**Argument**

- **clazz**: `class object`.

**Return**

- **`str`**: A string signature of function `class.__init__`.

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
sophon.utils.code_snippet(snippet)
```

Change a string-typed code snippet into Markdown-style code fence.

**Argument**

- **snippet**: `str`. A code snippet.

**Return**

- **`str`**: Markdown-style code fence.

---



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L158)</span>

## import_from_name

```python
sophon.utils.import_from_name(name)
```

Import module from string.

**Argument**

- **name**: `str`. Such as `foo`, `foo.someclass` or `foo.somefunction`.

**Return**

- **`module`**: It could be module-typed, class-typed or function-typed.

---



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/utils.py#L174)</span>

## generate_repo_link

```python
sophon.utils.generate_repo_link(obj, repo_url, branch)
```

Get the definition position of obj in source file, then link it to GitHub repo.

**Arguments**

- **obj**: `function object` or `class object`.
- **repo_url**: `str`. such as `https://github.com/yourusername/yourrepo`
- **branch**: `str`. repo branch.

**Return**

- **`str`**: Return the hyperlink of obj.

---



# sophon/build.py



<span style="float:right;">[[source]](https://github.com/monitor1379/sophon/blob/master/sophon/cmd/build.py#L26)</span>

## build_from_yaml

```python
sophon.cmd.build.build_from_yaml(config_fn)
```

Build documentations of python project given the configuration filename.

**Argument**

- **config_fn**: `str`. Sophon configuration filename.

**Return**

`None`

---


# Sophon

## What is Sophon?

Sophon is a tool that could automatically generate Markdown-format API documentation from Python code. 

~~~python
fuck
~~~

**markdown API documentation automatic generator** that 

makes it easy to create
intelligent and beautiful documentation,
written by Zhenpeng Deng and licensed under the MIT license.

## Why Sophon?

Features:

- Flexible.
- Markdown formats.
- Automatically generate API documentation.
- Works on Windows, Linux and macOS.


### What does "Sophon" mean?

**Sophon** is the official translation of "**智子**" in 《Rememberance of Earth's Past II: The Dark Forest》
which is written by the famous Chinese science fiction writer named **Cixin Liu(刘慈欣)**.


**Sophon** is a word amalgamation of `Sophia/sophist/sophisticated`, meaning **wisdom**, 
and `Proton/Electron/Neutron/Photon`, meaning **particle**,
consisting of a supercomputer embedded into a single proton that could fold itself to eleven space dimensions.
## Installation


## Usage

- Extra python file.

Extra the docstring of `py-file` into `md-file`.
Sophon will create a new markdown file if `md-file` argument isn't given.

Given a python file named 'test.py':

    """Here is Title
    
    This is module abstraction.
    
    
    Here is some example code of how to use this module.
    
    ```python
    def how_to_use():
        pass
    ```
    """
    
    
    def foo(bar, baz=90):
        """function description.
        can new line.
    
        # Argument:
            bar: str.
            some description of bar.
    
            baz: or some description here.
    
        # Return:
            None
    
        # Note:
            This is note of function.
    
        # Example:
            you can use `foo` in this way.
    
            ```python
            foo('dzp')
            foo('dzp', 22)
            ```
    
        """
        pass
       

This way can generate markdown document.
```bash
$ sophon generate <py-file> [output-md-file]
```

If `output-md-file` argument is not given,
then Sophone will generate a markdown file with the same name as py-file in current directory.

    # Here is Title
        
    This is module abstraction.
    
    
    Here is some example code of how to use this module.
    
    ```python
    def how_to_use():
        pass
    ```
    
    ## foo 
    ```
    test.foo(bar, baz=90)
    ```
    
    function description.
    can new line.
    
    ### Argument
    
    - bar: str.
    some description of bar.
    
    - baz: or some description here.
    
    ### Return
    None
    
    ### Note
    This is note of function.
    
    ### Example
    you can use `foo` in this way.
    
    ```
    foo('dzp')
    foo('dzp', 22)
    ```

 


```bash
$ sophon compile <md-file>
```

```bash
$ sophon <py-file> [md-file]
```

- Build markdown file.


- project mode.


more information in here:[A Guide to Sophon documentation](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)


## "What does "Sophon" mean?"

"Sophon"是刘慈欣著名作品《三体2：黑暗森林》中的"智子"一词的官方英文翻译。

"Sophon"是一个复合词，在英文中，"soph-"通常表示"智慧"的意思，比如"sophist"为"哲学家"，
"sophisticated"为"复杂玄妙的"的意思。
而"-on"表示"粒子"，比如离子（ion），电子（Electron），质子(proton)，中子（Neutron），强子（hadron），
玻色子（boson），胶子（Gluon），光子（photon）等等。

在原著中，智子表示的是一种能够将自身折叠到11维粒子的超级计算机。
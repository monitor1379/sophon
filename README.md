# What is Sophon
 
 Sophon is a tool that auto documenting from Python code to Markdown.

## Features

- written in Python

- works on Windows, Linux and Mac

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


《三体2：黑暗森林》译者刘宇昆在书中的注解如下：
> Translator's Note: There is a pun in Chinese between the word for a proton, 
> zhizi (质子), and the word for a sophon, zhizi (智子).
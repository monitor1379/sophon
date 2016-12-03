# Sophon Style Python Docstrings


!!! note "See also"

    - [Example Google Style Python Docstrings][1]

    - [Example NumPy Style Python Docstrings][2]

  

[1]: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google
[2]: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy



This is a module named `example.py`, which represents
how to write the docstrings of `module`, `function`, `class` and `method`.

~~~
# -*- coding: utf-8 -*-
"""Short description of module.

Long description of module.
Can be multiline.
"""

def example_create(name, age=0, sex='male', **kwargs):
    """Short description of function.
    
    Long description of function.
    Can be multiline too.
    
    # Arguments
        name: `any`. Description of name.
        age: `int`. Description of age. Defaults to zero.
            If it is multiline then must indent the following lines.
        sex: `str`. Description of sex. Defaults to 'male'.
        **kwargs: `dict`.
    
    # Return
        `Person`: an instance object of `Person` class with given information.
    
    # Note
        Here is note.
    
    # Examples
        Here is examples.
        ```
        jzm = example_create('jzm')
        batman = example_create('Bruce Wayne', 28, 'male')
        ```
    
    """
    pass


Class Person(object):
    """Short description of class.
    
    Long description of class.
    Can be multiline too.
    
    # Arguments
        name: `any`. Description of name.
        age: `int`. Description of age. Defaults to zero.
            If it is multiline then must indent the following lines.
        sex: `str`. Description of sex. Defaults to 'male'.
        **kwargs: `dict`.
    
    # Note
        Here is note.
    
    # Examples
        Here is examples.
        ```
        jzm = Person('jzm')
        batman = Person('Bruce Wayne', 28, 'male')
        ```
    
    """
    
    def __init__(self, name, age=0, sex='male', **kwargs):
        pass
        
    def speak(self, message):
        """Short description of method.
    
        Long description of method.
        Can be multiline too.
        
        # Arguments
            message: `str`. Description of message.
        
        # Return
            `None`.
            
        # Note
            Here is note.
        
        # Examples
            Here is examples.
            ```
            batman = example_create('Bruce Wayne', 28, 'male')
            batman.speak('I am batman!')
            ```
        """
        pass
~~~

<!--

~~~
# -*- coding: utf-8 -*-
"""Example Sophon style docstrings.

# Sophon style Python docstrings
    这个模板用来阐述如何编写Sophon风格的Python docstrings。
    因为Sophon风格的Python docstrings主要由Sophon来解析成Markdown文本，
    所以Sophon风格的Python docstrings采取了类Markdown的写法，
    绝大部分的Markdown文本都会被原样保留，比如：粗体、斜体、超链接、图片链接、
    列表、引用、表格、代码框等等，但是除了以下几样会被Sophon解析的时候进行加工：
   
    - 小节标题。一个小节的标题由一个井号与一行字符串组成，该小节的所有内容从该标题的第二行开始。
    与Markdown不同，小节的内容必须比该小节的标题向右多一个缩进（4个空格宽度）。
    所有的小节标题都会被解析成加粗文本，比如：
    ```text
    # Example
        This is some contents of "Example" section.
    ```
    会被Sophon解析成如下的Markdown文本：
    ```text
    **Example**
    This is some contents of "Example" section.
    ```
    
    - 小节列表。直接看例子：
    ```text
    # Arguments
        a: `int`. Description of a.
        b: `str`. Description of b.
            Here is still description of b.
        c: `any`. 
    ```





# Example
    例子小节可以使用"Example"或者"Examples"作为小节标题。
    小节的内容支持任何Markdown格式的文本。
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any Markdown formatting.

如果某个小节后面有向左缩进了的文本，则表示该小节的末尾到此为止。
另外如果某个小节后面有另外一个小节标题，则表示一个新的小节被创建了。
Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.



# Attributes
    module_level_variable1: `int`. Module level variables are only documented in
        the ``Attributes`` section of the module docstring.

"""

module_level_variable1 = 12345

module_level_variable2 = 98765
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""


def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
~~~
-->
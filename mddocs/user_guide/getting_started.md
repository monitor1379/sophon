# Getting started

Now let's create your first API documentation. 

Assuming the path of your Python module is `E://myproject//mycode.py`,
and the code is:

```
def hello_world(message):
    """Speak a message.

    Speak a message to the world.
    
    # Argument
        message: `str`. The message you want to speak.
               
    # Return
        `None`.
    """
    pass
```


Getting started is super easy:

```
$ sophon new
[2016-11-25 09:44:48,809][INFO]: Creating Sophon configuration file: sophon.yml...
[2016-11-25 09:44:48,812][INFO]: Create done!
```

1 seconds latter the configuration file `sophon.yml` has been created for you.

`sophon.yml` is the only configuration file, 
it decides which documentation of classes or functions will be generated and inserted to where.
Note that the `sophon.yml` is not necessary to be in the same directory as `mycode.py`.

Open the `sophon.yml`, edit it:
```python 
code_dir: E://myproject
build_dir: api
pages:
- page: API_of_mycode.md
  tags:
  - tag: 
    functions:
    - mycode.speak
```

- `code_dir` means the path of your Python project, 
this path will be add to the `sys.path` by Sophon so Sophon can `import` it.
Note that it can be absolute path or relative path to `sophon.yml`.

- `build_dir` means the directory of output documentations.
Note that it can be absolute path or relative path to `sophon.yml`.

- `pages` includes a list of `page`, each `page` means a Markdown file.




```
# encoding: utf-8


class Person(object):
    """This is a class of Person.

    # Arguments
        name: `str`. The name of the Person instance.
        age: `int`. Defaults to 18. The age of the Person instance.

    # Examples
        You could create a Person instance in this way:
        ```python
        batman = Person('Bruce Wayne')
        elder = Person('you-know-who', 99)
        ```
    """

    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        self.sex = 'male'

    def speak(self, message):
        """Speak something.

        # Argument:
            message: `str`. Something to speak.

        # Return:
            `None`.
        """
        print('[{}]: {}'.format(self.name, message))

```


Example Sophon Style Python Docstrings


# TODO

ref:

http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google
http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy
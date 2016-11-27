# Getting started

## 1. Write docstring 
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

## 2. Create configuration file

Getting started is super easy.

```
$ pwd
E://myproject

$ sophon new
[2016-11-25 09:44:48,809][INFO]: Creating Sophon configuration file: sophon.yml...
[2016-11-25 09:44:48,812][INFO]: Create done!
```

1 seconds latter the configuration file `E://myproject//sophon.yml` has been created for you.

`sophon.yml` is the only configuration file, 
it decides which documentation of classes or functions will be generated and inserted to where.
Note that the `sophon.yml` is not necessary to be in the same directory as `mycode.py`.

Open the `sophon.yml`, edit it:
```python 
code_dir: .
build_dir: api
pages:
- page: API_of_mycode.md
  tags:
  - tag: 
    functions:
    - mycode.hello_world
```

- `code_dir` means the path of your Python project, 
this path will be add to the `sys.path` by Sophon so Sophon can `import` it.
Note that it can be absolute path(such as `E://myproject`) or relative path(such as `.`) to `sophon.yml`.

- `build_dir` means the directory of output documentations,
every Markdown file of page is built in here, such as `E://myproject//api//API_of_mycode.md`.
Note that it can be absolute path or relative path to `sophon.yml`.

- `pages` includes a list of `page`, each `page` means the relative path of a Markdown file to `build_dir`.

## 3. Build Documentation

Use the following command to build documentation.
```bash
$ sophon build
```

If current path is not in the same directory as `sophon.yml`,
then you must specify it in the command.
```bash
$ pwd
D://somewhere

$ sophon build -f E://myproject//sophon.yml
```

If there are no ERROR in the log, then it is built successfully.
```
[2016-11-26 09:22:33,447][INFO]: Specify config_file:sophon.yml
[2016-11-26 09:22:33,448][INFO]: Loading configuration file: E:\myproject\sophon.yml
[2016-11-26 09:22:33,453][INFO]: Using repo_url: None
[2016-11-26 09:22:33,454][INFO]: Using branch: master
[2016-11-26 09:22:33,456][INFO]: Using code dir: E:\myproject
[2016-11-26 09:22:33,457][INFO]: Using template dir: None
[2016-11-26 09:22:33,457][INFO]: Using build dir: E:\myproject\api
[2016-11-26 09:22:33,459][INFO]: Creating build_dir...
[2016-11-26 09:22:33,461][INFO]: Create done
[2016-11-26 09:22:33,463][INFO]: ===========================
[2016-11-26 09:22:33,463][INFO]: Building file: API_of_mycode.md
[2016-11-26 09:22:33,464][INFO]: Using template file: None
[2016-11-26 09:22:33,464][INFO]: No template to load
[2016-11-26 09:22:33,466][INFO]: Creating page...
[2016-11-26 09:22:33,467][INFO]: Create done
[2016-11-26 09:22:33,469][INFO]: -------------------------
[2016-11-26 09:22:33,470][INFO]: Current tag: None
[2016-11-26 09:22:33,473][INFO]: generateing doc...
[2016-11-26 09:22:33,477][WARNING]: API_of_mycode.md has a tag without name. markdown doc will append to the file.
[2016-11-26 09:22:33,480][INFO]: Writing doc to page...
[2016-11-26 09:22:33,483][INFO]: Write done
```


Open `E://myproject//api//API_of_mycode.md` and you will see:

    ## hello_world
    
    ```python
    mycode.hello_world(message)
    ```
    
    Speak a message.
    
    Speak a message to the world.
    
    **Argument**
    
    - **message**: `str`. The message you want to speak.
    
    **Return**
    
    `None`.
    
    ---

Easy, right?

Now let's add a Python Class `Person` to `mycode.py`:

```
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


Edit `sophon.yml`:

```python
code_dir: .
build_dir: api
pages:
- page: API_of_mycode.md
  tags:
  - tag:
    functions:
    - mycode.hello_world
    classes:
    - mycode.Person
```

Run `sophon build` again, and you will see there is a new description of `Person` in `API_of_mycode.md`,
But it doesn't include the description of `Person.speak`.

So continuously edit `sophon.yml`:

```python
code_dir: .
build_dir: api
pages:
- page: API_of_mycode.md
  tags:
  - tag:
    functions:
    - mycode.hello_world
    classes_with_methods:
    - mycode.Person
```

Now you can see the documentations of both `Person` and `Person.speak`.

## 4. Use templates

In Sophon, template file is also Markdown file, but it includes **tags**,
Such as `{{tag_name}}`.

Tags are like placeholders, they are used to replaced by the generated Markdown text.
Each tag has a tag name, which is named in `sophon.yml`.
If use templates, then you must specify a `template_dir`:

```python
code_dir: .
template_dir: temp
build_dir: api
pages:
- page: API_of_mycode.md
  template: API_of_mycode.md
  tags:
  - tag: tag0
    functions:
    - mycode.hello_world
```

In this case, template file `E://myproject//temp//API_of_mycode.md` is the template file 
of documentation `E://myproject//api//API_of_mycode.md`.
This template file has a tag named `tag0`:

```markdown
# This is My First Documentation

{{tag0}}

Template file can include many tags.
```

After running `sophon build`, `E://myproject//api//API_of_mycode.md` will become this:

~~~markdown
# This is My First Documentation

## hello_world

```python
mycode.hello_world(message)
```

Speak a message.

Speak a message to the world.

**Argument**

- **message**: `str`. The message you want to speak.

**Return**

`None`.

---



Template file can include many tags.
~~~
    
Note that:

- if a tag don't have a name, then its Markdown text will append to the tail.
- if template Markdown file has a tag which is not specified in `sophon.yml`, Sophon will do nothing to it.


# 5. More details

More details of configuration can see **[User Guide/Configuration](configuration.md)**.

More details of docstring can see **[User Guide/Sophon Style Python docstrings](sophon_style_python_docstrings.md)**.


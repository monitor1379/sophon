# Sophon: Automatic API Markdown Documentation Generation for Python

More details about installation and usage of Sophon are in here: [Sophon](https://monitor1379.github.io/sophon).

## What is Sophon?

Sophon is a tool that could **automatically generate Markdown-format API documentations** from Python docstring,
just like **Epydoc** (supports reStructuredText, Javadoc, plaintext)
and **Napoleon** (Sphinx extension that enables Sphinx to parse both NumPy and Google 
style docstrings to reStructuredText).

Sophon is written by [Zhenpeng Deng(monitor1379)][1] and licensed under the MIT license.

## Why Sophon?

Features:
 
- **Support different kinds of docstrings.**
    Sophon mainly supports to parse docstring with the following styles and converts them to Markdown: 
    - Sophon style docstring
    - (Coming Soon) [Google style][4], the style recommended by [Khan Academy][5]
    - (Coming Soon) [NumPy style][6]
    
    Sophon also supports to parse every docstring in Python project,
    including docstrings on: `classes`, `methods` and `functions`
    (`modules`, `attributes` and `variables` will be supported soon)
    
    
- **Output Markdown format documentations.**
    Markdown is a way to write contents for the web.
    Unlike cumbersome word processing applications or other markup languages with complicated syntax,
    text written in Markdown can be easy to read, easy to write and easily shared for between computers, 
    mobile phones, and people. 
    Though it does not do anything fancy like change the font size, color or type by itself,
    it has enough stuffs to write an API documentation for your python projects.
    
    Another important reason of choosing Markdown is that there are some remarkable tools for Markdown
    to build beautiful documentations or blogs such as
    [MkDocs(Project documentation with Markdown)][2] or [Hexo(A fast, simple & powerful blog framework)][3].
   
- **Easily and Highly customizable.**
    Sophon uses [YAML: YAML Ain't Markup Language][7] as the format of configuration file.
    By configuring and providing Markdown template files, you can freely organize your documentation,
    or open some advanced features such as linking API to source files deposited on GitHub repositories.

- **One-Command build.** 
    you only need one command to build you API documentation.


You can find more details in **[User Guide/Installation](user_guide/installation.md)** or
**[User Guide/Getting Started](user_guide/getting_started.md)**.


## What does "Sophon" mean?

**Sophon** is the official translation of "**智子**" in 《Rememberance of Earth's Past II: The Dark Forest》
which is written by the famous Chinese science fiction writer named **Cixin Liu(刘慈欣)**.


**Sophon** is a word amalgamation of `Sophia/sophist/sophisticated`, meaning **wisdom**, 
and `Proton/Electron/Neutron/Photon`, meaning **particle**,
consisting of a supercomputer embedded into a single proton that could fold itself to eleven space dimensions.


[1]: https://github.com/monitor1379
[2]: http://www.mkdocs.org
[3]: https://hexo.io
[4]: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google
[5]: https://sites.google.com/a/khanacademy.org/forge/for-developers/styleguide/python#TOC-Docstrings
[6]: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy
[7]: http://www.yaml.org/
[8]: user_guide/sophon_style_python_docstrings

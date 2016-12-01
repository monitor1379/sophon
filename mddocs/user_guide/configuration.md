# Configuration

# Project information

`sophon.yml` must contain following information.

## code_dir

指定您Python项目所在的文件夹。

- Sophon会将该目录插入到`sys.path`中，以让Python解析器能够import。
- `code_dir`支持相对路径。如果是相对路径则是相对于`sophon.yml`而言。
- 可以不指定`code_dir`，默认为`.`。

---

## template_dir

存放Markdown模板的文件夹。
模板文件就是Markdown文件，只不还包含了一些形如`{{tag_name}}`的标记。更多详细用法请看`tags`。

- `template_dir`支持相对路径。如果是相对路径则是相对于`sophon.yml`而言。
- 可以不指定`template_dir`，默认为`None`。
- 不指定`template_dir`表示不使用模板功能，此时后续的某个文档`page`项包含了`template`项，则会报错。

---

## build_dir

生成的API文档所存放的文件夹。

- `build_dir`支持相对路径。如果是相对路径则是相对于`sophon.yml`而言。
- 可以不指定`build_dir`，默认为`./api`，即在`sophon.yml`所在文件夹新建一个叫做`api`的文件夹来存放API文档。

---

## repo_url

指定存放了源代码的仓库，可以在API文档中为每个API生成一个链接到源代码的超链接。

- 暂时仅支持GitHub。
- 格式为`https://github.com/your_user_name/your_repo`。
- 可以不指定`repo_url`，默认为`None`。
- 不指定`repo_url`表示不使用该功能。

---

## branch

指定源代码仓库上的分支。

- 可以不指定`branch`，默认为`master`。
- 当不指定`repo_url`时，`branch`无效。

---

## style

指定您Python代码中docstring所使用的风格。

- 目前支持`sophon`(`google`, `numpy`即将支持)。
- 可以不指定`style`，默认为`sophon`。

---

## pages

`pages`是一个包含了0个或多个`page`的列表，包含了所有要生成的文档。更多详细用法请看`page`。

- 可以不指定`pages`，默认为`None`。
- 当不指定`pages`或指定了`pages`但是不包含任何`page`时，表示不生成任何文档。

---

## page

`page`表示一个生成的API Markdown文档。格式为：

```text
# filename: /home/user/sophon.yml
build_dir: api
template_dir: templates

pages:
- page: test/aa.md
  template: bb.md
- page: cc.md
  template: test/dd.md
``` 

- 每个`page`必须指定文件路径名，该文件路径名必须是相对路径，且是相对于`build_dir`而言。
- 在上面的例子中，Sophon会按顺序：
    - 生成路径名为`/home/user/api/test/aa.md`的API文档，
    所使用的模板文件为`/home/user/templates/bb.md`。
    - 生成路径名为`/home/user/api/cc.md`的API文档，
    所使用的模板文件为`/home/user/templates/test/dd.md`。

---

## tags

`tags`是一个包含了0个或多个`tag`的列表，也是`page`的成员。更多详细用法请看`tag`。

- 可以不指定`tags`，默认为`None`。
- 当不指定`tags`或指定了`tags`但是不包含任何`tag`时，Sophon不会向该`tags`所属`page`文件中生成任何Markdown text。

---

## tag

`tag`表示一个标记，通常结合模板文件来使用，表示生成的API Markdown text应该插入到模板文件的哪个地方。

举个例子,假设模板文件`/home/user/templates/bb.md`内容为：
```text
# Hello World

{{tag0}}

## Hello Sophon

{{tag1}}
```

配置文件为：
```text
# filename: /home/user/sophon.yml
build_dir: api
template_dir: templates

pages:
- page: test/aa.md
  template: bb.md
  tags:
  - tag: tag0
    functions:
    - mod.func
  - tag: tag1
    classes:
    - mod.clazz
``` 


则运行Sophon之后：

- Sophon会先读取模板文件`/home/user/templates/bb.md`里的内容；
- 然后将标记`{{tag0}}`替换为函数`mod.func`的API Markdown text；
- 再将标记`{{tag1}}`替换为类`mod.clazz`的API Markdown text；
- 最后将内容写入`/home/user/api/test/aa.md`中。


注意的是，以下几种情况中，该tag下包含的函数、类的API Markdown text会依次添加在文件末尾，而不是替换掉模板文件中的`{{tag}}`：

- 配置文件中指定了一个tag，但是没有给tag名时；
- 配置文件中指定了一个tag，但是在模板文件中不存在该tag标记时；
- 配置文件中指定了一个tag，但是该tag所属的`page`没有使用模板文件时。

每个tag所包含的API按照固定顺序classes->classes_with_members->functions依次生成API Markdown text。

另外，Sophon不会对存在于模板文件但是却没有在配置文件中指定的tag作任何处理，也就是一切以配置文件为准。

---

## classes

`classes`是一个包含多个类的包路径的列表。

Sophon在生成一个类的API文档时，只会选择该类的docstring来生成该类构造函数的API Markdown text，
并不包括该类的成员函数与方法。

---

## classes_with_methods

`classes_with_methods`是一个包含多个函数的包路径的列表。

Sophon在生成一个类的API文档时，会生成包括构造函数在内的该类所有公有成员函数与方法的API Markdown text。

---

## functions

`functions`是一个包含多个函数的包路径的列表。

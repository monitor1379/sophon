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

```
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

举个例子：
```
# filename: /home/user/sophon.yml
build_dir: api
template_dir: templates

pages:
- page: test/aa.md
  template: bb.md
  tags:
  - tag:
  functions:
  
``` 


---

## functions

---

## classes

---

## classes_with_methods

---


## Hierarchy of configuration file

```

# 可以没有，默认为None
pages:

# 如果有page，则在build_dir/下生成名为page的文件
- page: index.md

- page: user/bb.md  # build_dir/user/bb.md
  # 如果指定了该文件的模板，且template_dir存在，则使用模板。
  # 如果指定了该文件的模板，而template_dir不存在，则报错
  # 如果指定了该文件的模板，且template_dir存在，但模板文件不存在，则报错
  # 如果没有指定该文件的模板，则不用模板，即创建空白page然后添加doc到文件末尾
  template: user/bb.md  # template_dir/user/bb.md


- page: cc.md
  template: cc_temp.md
  # 如果没有tags，则不从代码中生成markdown。
    # 如果指定了模板文件，则page内容为模板文件的内容
    # 如果没有指定模板文件，则page内容为空
  # 如果有tags，则对每个tag生成markdown
    # 如果指定了template，则将template文件中的每个{{tag标记}}置换为对应的markdown
    # 如果没有指定template，tags的位置作用失效，所有markdown添加到文件末尾
  tags:
  # 每一个tag都有一个tag名，用于表示doc在文件中的位置
  # 如果有tag名，则置换{{tag}}为markdown内容
  # 如果没有tag名，则生成的doc添加在page的末尾
  # 如果tag内容为空，则表示markdown doc为空字符串''

  - tag: tag1
    # 每个tag的doc生成顺序并不是tag内部决定，而是classes->classes_with_members->functions
    functions:
    - sss.gates.foo
  - tag: tag2
    classes:
    - sss.gates.Dense
    - sss.gates.Person
    # 后续支持
    # classes_with_members:
```


## Simple example of configuration file

Let's see an simple example of configuration file.

```
TODO
```

## Complex example of configuration file

Let's see an complex example of configuration file.

```
TODO
```

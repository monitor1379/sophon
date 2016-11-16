# Features

- 从Python code中自动生成api文档
- 支持templates与{{sophon}}标记
- 使用yml配置文件来指定生成文档
- yml支持格式：

```
root: 
url:
pages:
  - page:
    name: aa.md
    tags:
      - tag:
        name: tag1  # 如果这个tag在aa.md文件中不存在，则拼接在文件末尾
        functions:  # 显示函数的doc，可以是类的方法或者静态方法
          - mod1.func  # 显示模块mod1中的函数func的doc
          - mod1.class1.func  # 显示模块mod1中的类class1中的方法func的doc
        classes:  # 显示类的doc，与构造函数
          - mod1.class1  # 显示模块mod1中的类class1的类doc以及构造函数
          
      # 以下方法暂未支持
      - tag:
        name: tag2
        all_functions:  # 显示某个模块或者某个类下的所有函数
          - mod2  # 显示模块mod2中的所有直属函数的doc，不包含class2的方法
          - mod2.class2  # 显示模块mod2中的类class2的所有方法的doc
        all_classes:  # 显示某个模块下类的doc，与构造函数
          - mod3
        all_classes_and_its_functions:  # 显示某个模块下类的doc，构造函数，以及类的所有方法，包括静态方法
          - mod4
        all:  # all_functions + all_classes_and_its_functions的并集
         - mo5
```  
    
    
# TODO

- 后续可以增加更多的{{tag}}，支持像sphinx的autodoc插件那种`.. pymodule: module_name`的功能。
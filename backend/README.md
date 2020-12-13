# backend

QARobot后端,主要的功能函数写在./robot/view.py里面

## 项目结构

* backend 文件夹-项目设置文件夹  
* robot 文件夹-项目主程序文件夹

URL设置，在`./robot/urls.py`中配置URL及其方法

## 项目配置

项目启动前，需要对数据库进行初始化，命令如下

```shell
python3 manage.py migrate
```

启动项目的命令
```shell
python3 manage.py runserver
```

## 依赖

* django
* bf4
* jieba
* numpy

spacy需要安装en库
```
python3 -m spacy download en
```

源代码安装方式
```shell
git clone 目标url
cd 目标文件夹
python3 setup.py build
python3 setup.py install
```
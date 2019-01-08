#安装指南
## 环境
* ubuntu 18.04
* mysql-5.8
    [安装教程](https://blog.csdn.net/lynnyq/article/details/80296137)
    ```
    ubuntu18.04 mysql root账户登陆。默认通过验证root身份通过，不使用密码
    可新建用户进行管理
    ```

* python2.7和相关依赖
    ```
    pip install -r requirement.txt
    ```
## 配置
* 数据库
    ```mysql
    create database cuit_acm (CHARACTER SET =utf8);
    create database competition (CHARACTER SET =utf8);
    ```
  > 注意数据库字符编码要为utf-8，不然无法存储中文
* 数据表
    + 通过initDB.py初始化表
* secret.py 保存有网站管理私密信息
    ```python
    class Security:
        def __init__(self):
            self.key = "BHC#@*UM" # Key
            self.iv = "\x22\x33\x35\x81\xBC\x38\x5A\xE7"
    security = Security()
    SQL_USERNAME="test"
    SQL_PASSWORD="123456"
    MAIL_PASSWD="123456"
    ```


## 数据表备注
* user 本网站用户
    + remark 签名
    + rights 权限
        ```python
        {1:"训练中",2:"教练",4:"管理员",8:"待审核"}
        ```
    + college 学院
        ```python
        {0: '软工'}
        ```
    + situation 经历和去向
    + active 是否退役
* account oj账号


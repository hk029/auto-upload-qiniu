# 准备
## 安装qiniu
	pip install qiniu
## 安装PIL
64位的直接安装（链接: http://pan.baidu.com/s/1nvD7Rbr 密码: ey8s）

32位的需要在网站下载：http://www.pythonware.com/products/pil/

## 安装pyqt4
https://riverbankcomputing.com/software/pyqt/download

## 安装pywin32
https://sourceforge.net/projects/pywin32/files/?source=navbar

根据你自己系统和python的版本选择

## 修改config.ini
- ak sk填自己七牛的秘钥

![your text](http://o7bk1ffzo.bkt.clouddn.com/1463834793689)

- bucket填自己的七牛资源的名称

![your text](http://o7bk1ffzo.bkt.clouddn.com/1463834826744)

- url 填七牛前缀

![your text](http://o7bk1ffzo.bkt.clouddn.com/1463835143145)

注意：最后要加上一个斜杠'/'

- dir填本机缓存图片的目录（要存在这个文件夹,如果没有要新建一个）

![your text](http://o7bk1ffzo.bkt.clouddn.com/1463834858628)

# 运行auto-upload.ahk
然后按ctrl+alt+s开启剪贴板监控服务
运行后会出现一个空白的对话框，如果你复制东西，这里面会有显示

![your text](http://o7bk1ffzo.bkt.clouddn.com/1463833884730)


![your text](http://o7bk1ffzo.bkt.clouddn.com/1463833945050)

按ctrl+alt+a就可以截屏（使用qq截屏功能）

# 本文参考
[Python如何获取Windows剪贴板内容并判断类型？](https://www.zhihu.com/question/37741420)


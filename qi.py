# -*- encoding:utf-8 -*-
from qiniu import Auth, put_data, put_file
from time import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import win32clipboard as w
import win32con
from PIL import ImageGrab
import ConfigParser as CP
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#切换到当前目录下
os.chdir(sys.path[0])

conf = CP.ConfigParser()
conf.read('config.ini')


accessKey = conf.get('qiniu', 'ak') # AK
secretKey = conf.get('qiniu', 'sk') # SK
bucket_name = conf.get('qiniu', 'bucket') # 七牛空间名
url = conf.get('qiniu', 'url') # url
mydir = conf.get('qiniu', 'dir') # url

def get_image():
    '''get Image from clipboard'''
    im = ImageGrab.grabclipboard()
    if im is not None:
        now = int(time() * 1000)
        filename = '%s.png' % now
        filepath = mydir + filename
        im.save(filepath)
        return filepath
    else:
        return False
 
def upload_data(data, bucket_name):
    #生成上传凭证
    q = Auth(accessKey, secretKey)
    key = str(int(time() * 1000))
    token = q.upload_token(bucket_name, key) 
    #上传文件
    retData, respInfo = put_data(token, key, data)
  
    return 'o7bk1ffzo.bkt.clouddn.com/' + key

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

def on_clipboard_change(): 
    imgpath = get_image()
    if imgpath == False:
        data = clipboard.mimeData() 
        if data.hasFormat('text/uri-list'): 
            for path in data.urls(): 
                upload2qiniu(path.toString()[8:])
        if data.hasText(): 
            print data.text() 
    else:
        upload2qiniu(imgpath)

def upload2qiniu(imgpath):
    with open(imgpath , 'rb') as f:
        url = upload_data(f.read(), 'mypic')
        text = '![your text](http://%s)' % url
        setText(text)


if __name__ == '__main__':
    #  if len(sys.argv) == 2:
  #      imgpath = sys.argv[1]
  #  else:
  #      imgpath = get_image()

    app = QApplication([]) 
    clipboard = QApplication.clipboard()
    clipboard.dataChanged.connect(on_clipboard_change)
    app.exec_()

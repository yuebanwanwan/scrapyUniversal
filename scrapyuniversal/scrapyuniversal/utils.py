from os.path import realpath,dirname
import  json


def get_config(name):
    #dirname() 获取当前脚本运行的绝对路径
    path = dirname(realpath(__file__)) + '/config/' + name + '.json'
    with open(path,'r',encoding='utf-8') as f:
        return json.loads(f.read())
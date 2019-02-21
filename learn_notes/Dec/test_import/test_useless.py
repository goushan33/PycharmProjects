import asyncio,inspect
import logging;logging.basicConfig(level=logging.INFO)

def add_route(fn):#编写一个add_route函数，用来注册一个URL处理函数
    print('ok')


def add_routes(module_name):#module_name应该是存放一系列url处理函数的文件
    n=module_name.rfind('.')#在model_name字符串中查找子字符串'.'的位置，返回坐标。未找到返回-1

    if n==-1:
        mod = __import__(module_name, globals(), locals())
    else:
        name=module_name[n+1:]
        s=__import__(module_name[:n], globals(), locals(),[name],0)
        mod = getattr(s, name)

    for attr in dir(mod):
        if attr.startswith('_'):#把导入的模块里面本身的属性；例如__builtins__\__cached__\__doc__等过滤掉
            continue
        print(attr)
        fn = getattr(mod, attr)
        if callable(fn):
            print(fn.__str__)
            print(fn.__name__)
        else:
            print('NO')

add_routes('import_module1')
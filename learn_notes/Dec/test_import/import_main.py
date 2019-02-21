def add_routes(module_name):#module_name应该是存放一系列url处理函数的文件
    n=module_name.rfind('.')#在model_name字符串中查找子字符串'.'的位置，返回坐标。未找到返回-1
    if n==-1:
        mod = __import__(module_name, globals(), locals())
    else:
        #如果module_name有'.'的话，应该是：包名.模块名（注意：包名是文件夹名，高一层）
        name=module_name[n+1:]
        #mod=getattr(__import__(module_name[:n],globals(),locals(),[name],0),name)
        #[name]:相当于fromlist = ('name',)，也可以写成[name]
        s=__import__(module_name[:n], globals(), locals(),(name,),0)
        mod = getattr(s, name)
    print(mod)
    mod.hello()
    for attr in dir(mod):
        print(attr)

add_routes('test_import.import_module1')
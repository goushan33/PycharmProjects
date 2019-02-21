#深学习inspect 模块2018/12/03
import inspect

def test(a,b=1,*c,d,f=3,**e):
    print(a,b,c,d)

param=inspect.signature(test)
print(param)#(a, b=1, *c, d, **e)
s=param.parameters
for k,v in s.items():
    print(k,v)#{a: a,b:b=1……}
    # 返回参数类型：
    # POSITIONAL_OR_KEYWORD：位置参数或者默认参数
    # VAR_POSITIONAL:可变参数
    # KEYWORD_ONLY：命名关键字参数
    # VAR_KEYWORD：关键字参数
    print(str(v.kind))

    #返回默认值。若无，则返回<class 'inspect._empty'>
    print(v.default)

def get_required_kw_args(fn): #收集没有默认值的命名关键字参数
    args = []
    params = inspect.signature(fn).parameters #inspect模块是用来分析模块，函数
    for name, param in params.items():
        #KEYWORD_ONLY代表命名关键字参数
        if str(param.kind) == 'KEYWORD_ONLY' and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)#将没有默认值的命名关键字用tuple形式返回

print(get_required_kw_args(test))
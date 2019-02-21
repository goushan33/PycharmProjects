import hashlib,random

def register(username, password):
    usr=db[username]#usr是一个User类，User类包含username、password（md5格式的密码）、salt这三个属性
    usr.password= get_md5(password+username+usr.salt)
    return usr.password

def get_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()#上面三行换种写法：return hashlib.md5(password.encode('utf-8)).hexdigest()
#用一个dict模拟数据库，模拟用户登录过程
class User(object):
    def __init__(self,username,password):
        self.username=username
        self.salt=''.join([chr(random.randint(48,122))for i in range(20)])
        self.password=get_md5(password+username+self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user = db[username]
    if user.password==get_md5(username+password+user.salt):
        print('OK')
    else:
        print('NO')
login('bob','abc999')




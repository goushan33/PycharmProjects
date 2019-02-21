from wsgiref.simple_server import make_server
from browser_test1 import application
http_server=make_server('',8000,application)
print('servering http on port 8000……')
http_server.serve_forever()

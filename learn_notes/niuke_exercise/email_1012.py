from email.mime.text import MIMEText
gs_msg=MIMEText('傻逼，劳资在学PYTHON发邮件。哼！','plain','utf-8')

src_addr='18188609950@163.com'
src_psw='20180903gsinhk'
des_addr='470704291@qq.com'
smtp_server ='smtp.163.com'

import smtplib
server = smtplib.SMTP(smtp_server, 25)
#server.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
server.login(src_addr,src_psw)
server.send(src_addr,[des_addr],gs_msg.as_string())
server.quit()


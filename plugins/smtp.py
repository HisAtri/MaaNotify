import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, password, smtp_addr, smtp_port, smtp_tls):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    if(smtp_tls == 'TLS'):
        server = smtplib.SMTP(smtp_addr, smtp_port)
        server.starttls()  # 开启安全连接
    elif(smtp_tls == 'SSL'):
        server = smtplib.SMTP_SSL(smtp_addr, smtp_port)
    server.login(from_addr, password)  # 使用发件人的邮箱地址和密码登录
    text = msg.as_string()  # 将 MIMEMultipart 对象转换为字符串
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def smtp(subject,content):
    config = configparser.ConfigParser()
    config.read('config.ini')
    # 访问配置
    server = config['SMTP']['server']
    tls = config['SMTP']['tls']
    port = int(config['SMTP']['port'])
    from_user = config['SMTP']['username']
    password = config['SMTP']['password']
    to_user = config['SMTP']['to']

    send_email(subject=subject, message=content, from_addr=from_user, to_addr=to_user, password=password, smtp_addr=server, smtp_port=port, smtp_tls=tls)
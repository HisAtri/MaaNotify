# MAA Notify

支持SMTP

修改自<https://github.com/yokinanya/MaaNotify>

## 配置

```ini
[SMTP]
server = smtp.xms.mx
tls = TLS/SSL
port = 587/465
username = sender@xms.mx
password = password
to = user@xms.mx
```
- server：SMTP服务器地址
- tls/port：一般来说，tls=TLS时，port=587；tls=SSL时，port=465，根据实际使用的SMTP服务器决定。
- username：你的SMTP账号，即发件人邮箱
- password：你的SMTP密码，国内邮箱一般为授权码
- to：接收邮件的邮箱，你常用的邮箱

## 使用

基于Python标准库，无需额外安装环境。

```bash
python main.py
```
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 10:43
# @Author  : sunzhen
# @File    : 01 服务端.py
# @Software: PyCharm

import socket

server = socket.socket()

server.bind(('127.0.0.1', 8080))
server.listen()

while True:
	connect, addr = server.accept()
	data = connect.recv(1024)
	print(data)
	connect.send(b'HTTP/1.1 200 \r\n\r\n')
	# connect.send(b'<h1>hello!! </h1>')
	with open('a.txt', 'rb') as file:
		connect.send(file.read())
	connect.close()
	
	
'''
b'GET / HTTP/1.1\r\n	请求头
Host: 127.0.0.1:8080\r\n
Connection: keep-alive\r\n	请求体
Cache-Control: max-age=0\r\n
sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"\r\n
sec-ch-ua-mobile: ?0\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n
\r\n
get 没有请求体
'
'''


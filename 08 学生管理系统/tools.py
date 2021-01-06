# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 15:58
# @Author  : sunzhen
# @File    : tools.py
# @Software: PyCharm
import hashlib


def encrypt_password(password, x='sdaassad'):
	hashlib_password = hashlib.sha256()
	hashlib_password.update(password.encode('utf8'))
	hashlib_password.update(x.encode('utf8'))
	return hashlib_password.hexdigest()

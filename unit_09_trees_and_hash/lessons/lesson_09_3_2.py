"""
Хэш-подпись сообщения
"""

import hashlib

print(hashlib.sha1(b'Hello World!').hexdigest())
print(hashlib.sha1(b'Hello World.').hexdigest())
print(hashlib.sha1(b'qwerty' + b'Hello World.').hexdigest())

s = hashlib.sha1(b'Hello World.').hexdigest()
print(s.encode('utf-8'))
print(hashlib.sha1(b'qwerty' + bytes(s.encode('utf-8'))).hexdigest())

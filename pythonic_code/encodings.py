import sys

print(sys.version_info)
print(sys.version)

a = b'w\x69taj'
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # egzemplarz typu str

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

print(to_str(b'foo'))

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(b'foo')))

import locale
print(locale.getpreferredencoding())
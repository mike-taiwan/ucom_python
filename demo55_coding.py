# encoding=UTF-8
p=u'中文輸入'
print repr(p)
print repr(p.encode('UTF-8'))
print repr(p.encode('ms950'))
print repr(p.encode('big5'))
#print p.encode('ms950')

new_s = '\xe5\xad\x97'
print new_s
print repr(new_s)
new_latin = new_s.decode('latin-1')
print repr(new_latin)
print new_latin
new_utf8 = new_s.decode('utf-8')
print repr(new_utf8)
print new_utf8
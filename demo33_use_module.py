import demo32_module

print "demo33"

print demo32_module.foo(5, 6)
print demo32_module.bar(7, 8)

import demo32_module as d

print d.foo(9, 10), d.bar(11, 12)

from demo32_module import foo

print foo(13, 14)

from demo32_module import bar as b

print b(15, 16)

from demo32_module import foo as f1, bar as f2

print f1(17, 18), f2(19, 20)
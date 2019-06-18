# encoding=UTF-8
import itertools

result1 = itertools.chain('ABC', '123', 'abc')
print type(result1)
for p in result1:
    print p,

print'\nsecond times'
for p in result1:
    print p,
result2 = itertools.chain('ABC', '123', 'abc', u'甲乙丙丁')
list2 = [p for p in result2]
for l in list2:
    print l,
print
for l in list2:
    print l,
print

result3 = itertools.permutations('ABCDE', 3)
list3 = [x for x in result3]
print type(list3), list3
print len(list3)
result4 = itertools.combinations('ABCDEF', 2)
list4 = [x for x in result4]
print len(list4), list4
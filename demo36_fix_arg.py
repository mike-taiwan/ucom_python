def sample_fix(x1, x2, x3):
    print 'first element:', x1
    print 'second element:', x2
    print 'third element:', x3


sample_fix('apple', 'banana', 'citron')
sample_fix(*('apple', 'banana', 'citron'))
sample_fix('apple', *('banana', 'citron'))
sample_fix(*('7-11', 'Fami'), x3='OK')
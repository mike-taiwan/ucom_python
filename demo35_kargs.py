def sample_key_args(fix1, fix2, **kargs):
    print "fix part:", fix1, fix2
    for k, v in kargs.items():
        print 'key=%s, value=%s' % (str(k), str(v))


sample_key_args('hello', 'world')
sample_key_args(3.14, 1234)
sample_key_args('first sample', 'using key/value',
                course='BDPY', duration=35, instructor='Mark Ho')
myCourse = {'course': 'BDPY', 'duration': 35, 'instructor': 'MarkHo'}
sample_key_args('second example','using dictionary', **myCourse)
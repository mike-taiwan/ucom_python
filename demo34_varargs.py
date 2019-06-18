def sample_variable_arguments(fix1, fix2, *args):
    print "fix part1=%s, part2=%s" % (str(fix1), str(fix2))
    for p in args:
        print p


sample_variable_arguments('hello', 'world')
sample_variable_arguments(100, 200)
sample_variable_arguments('hi', 'sample1', 1, 2, 3, 4, 5)
sample_variable_arguments('hi', 'example2', 'abc', 'def', 'apple', 'banana')
courses = ['POOP', 'BDPY', 'PYKT']
sample_variable_arguments("i have", '3 courses', courses)
sample_variable_arguments("[II]i have", '3 courses', *courses)
courses_t = ('POOP', 'BDPY', 'PYKT')
sample_variable_arguments("[III]i have", '3 courses', *courses_t)
courses_s = {'POOP', 'BDPY', 'PYKT'}
sample_variable_arguments("[IV]i have", '3 courses', *courses_s)
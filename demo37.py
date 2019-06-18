def dumpUserInfo(name, id, location):
    print "user name:", name
    print "id:", id
    print "location:", location


dumpUserInfo("Mark", 12345, 'Taipei')
dumpUserInfo(name='Mark', id=54321, location='Hsinchu')
user1 = {'name': 'John', 'id': 33, 'location': "LA"}
dumpUserInfo(**user1)
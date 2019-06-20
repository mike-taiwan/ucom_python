from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from demo90_sqlalchemy import User, Base

engine = create_engine('sqlite:///:memory:', echo=True)
print([User.__tablename__, User.__table__])
Base.metadata.create_all(engine)

Session1 = sessionmaker(bind=engine)
session1 = Session1()
user1 = User(name='user1', fullname='User one', password='ucom')
user2 = User(name='user2', fullname='User two', password='uuu')
session1.add(user1)
session1.add(user2)
session1.commit()

# session1 = Session1()
all_users = session1.query(User)
for i in all_users:
    print "get a user:", i
# session1.commit()
session3 = Session1()
userToModify = session3.query(User).filter_by(name='user1').first()
print "[i]current dirty object list:", [session3.dirty]
userToModify.fullname = 'Mark Ho'
print "[ii]current dirty object list:", [session3.dirty]
session3.commit()
all_users2 = session3.query(User)
for i in all_users2:
    print "[II]:get a user:", i

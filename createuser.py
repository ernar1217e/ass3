from database import User, Session, engine,Address

local_session = Session(bind=engine)

new_user = User(name='Nick', fullname='Gagalia')
new_address = Address(email_address="e@email.com", user_id=1)

local_session.add(new_user)
local_session.add(new_address)

local_session.commit()
from database import User, Session, engine

local_session = Session(bind=engine)

def read_all_users():
    users = local_session.query(User).all()

    return users


def read_one_user(id):

    user = local_session.query(User).filter(User.id == id).first()

    return user

# print(read_one_user(3))
# print('\n')
# print(read_all_users())
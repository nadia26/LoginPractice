from pymongo import Connection

conn = Connection()
db = conn['people']

def add_user(user, password):
    d = {'uname': user, 'pword': password}
    db.people.insert(d)
    

def authenticate(user, password):
    pass

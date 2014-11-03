from pymongo import Connection

conn = Connection()
db = conn['people']

def add_user(username, name, password):
    d = {'username': username,'name':name, 'password': password}
    if check(username):
        return "error: username already there"
    else:
        db.people.insert(d)
        return "added user"
    

def authenticate(username, password):
    pass
#check to see if username & password match, if they do, will return true
def check(username):
    pass
#if the given username exists, it will return true

from rest_framework.exceptions import AuthenticationFailed
from rest_framework import exceptions
import jwt, datetime


def create_access_token(id):
    return jwt.encode({
        'id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
        'iat': datetime.datetime.utcnow()
     }, 'access_secret', algorithm='HS256')

def create_refresh_token(id):
    return jwt.encode({
        'id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
     }, 'refresh_secret', algorithm='HS256')

def decode_access_token(token):
    try:
        print(token)
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['id']
    except:
        raise exceptions.AuthenticationFailed('Unauthenticated')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['id']
    except:
        raise exceptions.AuthenticationFailed('Unauthenticated*')
import jwt
from datetime import datetime, timedelta
import os

secretKey = os.getenv('SECRET_KEY')

class Token:
    def generateToken(identity):
        experiationTime = datetime.utcnow() + timedelta(hours=24)
        payload = {
            'exp': experiationTime,
            'iat': datetime.utcnow(),
            'sub': identity
        }
        token = jwt.encode(payload, secretKey, algorithm='HS256')
        return token

    def decodeToken(token):
        try:
            # Decode the token using the secret key used for encoding
            decoded_token = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            return decoded_token
        except jwt.ExpiredSignatureError:
            return {'error': 'Token has expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
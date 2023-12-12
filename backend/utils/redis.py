import redis, os
from controller.userController import jwt

host = os.getenv('HOST')
portRedis = os.getenv('REDIS_PORT')

redis = redis.StrictRedis(
    host=host, port=portRedis, db=0
)

@jwt.token_in_blocklist_loader
def checkTokenIsRevoked(jwtHeader, jwt_payload: dict):
        jti = jwt_payload['tokens']
        redisToken = redis.get(jti)
        return redisToken is not None
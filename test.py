import redis

r = redis.Redis(host='127.0.0.1', port=6379,db=0)
# pipe = r.pipeline(transaction=True)

r.hset("dic_name","a1","aa")
r.hset("dic_name","b1","aa")
r.hset("dic_name","c1","aa")
print(r.hgetall("dic_name"))
len({})
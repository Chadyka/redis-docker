import redis

# connect to redis
r = redis.Redis(host='localhost', port=6379)

# set a key
r.set('test-key', 'test-value')
r.set('balga', 'bela')
# get a value
print(r.get('test-key'))

print(r.get('balga'))

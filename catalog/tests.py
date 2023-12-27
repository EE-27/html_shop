from django.test import TestCase

# Create your tests here.
import redis

# Replace these values with your actual Redis server information
redis_host = '127.0.0.1'
redis_port = 6379

try:
    # Create a connection to the Redis server
    r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    # Test the connection
    response = r.ping()
    print(f"Redis Ping Response: {response}")

except redis.exceptions.ConnectionError as e:
    print(f"Error connecting to Redis: {e}")
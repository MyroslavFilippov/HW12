import redis
import random

class ProbabilisticCacheRedisClient:
    def __init__(self, host='localhost', port=6379, db=0, cache_clear_prob=0.1):
        self.redis_client = redis.Redis(host=host, port=port, db=db)
        self.cache_clear_prob = cache_clear_prob

    def set(self, key, value, *args, **kwargs):
        return self.redis_client.set(key, value, *args, **kwargs)

    def get(self, key, *args, **kwargs):
        return self.redis_client.get(key, *args, **kwargs)

    def delete(self, key, *args, **kwargs):
        return self.redis_client.delete(key, *args, **kwargs)

    def probabilistic_cache_clear(self):
        # Retrieve all keys from Redis
        all_keys = self.redis_client.keys()

        # Calculate the number of keys to delete based on the cache_clear_prob
        num_keys_to_delete = int(len(all_keys) * self.cache_clear_prob)

        # Randomly select keys to delete
        keys_to_delete = random.sample(all_keys, num_keys_to_delete)

        # Delete the selected keys
        for key in keys_to_delete:
            self.redis_client.delete(key)

if __name__ == "__main__":
    # Example usage
    redis_client = ProbabilisticCacheRedisClient()

    # Set key-value pairs
    redis_client.set('key1', 'value1')
    redis_client.set('key2', 'value2')
    redis_client.set('key3', 'value3')

    # Get value by key
    print(redis_client.get('key1'))

    # Probabilistic cache clearing
    redis_client.probabilistic_cache_clear()
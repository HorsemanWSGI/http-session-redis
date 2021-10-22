from http_session_redis import RedisStore


def test_store(redisdb):
    store = RedisStore(redisdb, 300)
    store.set('test', {'this': 'is a session'})
    assert store.get('test') == {}

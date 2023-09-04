import redis from 'redis'

const client = redis.createClient()

const hashkey = "tim"
client.hset(hashkey, "Portland", 50, redis.print)
client.hset(hashkey, "Seattle", 80, redis.print)
client.hset(hashkey, "New York", 20, redis.print)
client.hset(hashkey, "Bogota", 20, redis.print)
client.hset(hashkey, "Cali", 40, redis.print)
client.hset(hashkey, "Paris", 2, redis.print)

client.hgetall(hashkey, (error, response) => {
    if (error) {
        console.error(error)
    }
    else if (response) {
        console.log(response)
    }
})

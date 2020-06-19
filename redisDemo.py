import redis

def main():
    cli=redis.Redis(host='10.10.10.130')
    cli.set('username','hello',ex=300)
    cli.set('nickname','张三')
    print(cli.get('nickname'))
    print(cli.get('nickname').decode())
    print(cli.get('username'))
    print(cli.get('username').decode())
    print(cli.ttl('username'))
    cli.set('yuting',300)
    cli.incr(('yuting'))
    print(cli.get('yuting'))
    cli.incrby('yuting',50)
    print(int(cli.get('yuting').decode()))
    cli.hset('stu1','id','1001')
    cli.hset('stu1','name','大宝')
    print(cli.hgetall('stu1'))
    print(cli.hget('stu1','name').decode())
    cli.rpush('list1',10,20,30,40)
    print(cli.lrange('list1',0,-1))



if __name__ == '__main__':
    main()
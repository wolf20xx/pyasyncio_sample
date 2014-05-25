import asyncio

@asyncio.coroutine
def put_meter(name, number):
    def accum_str(num):
        s = ""
        return s.join(["#" for x in range(0 , num)])
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)...: %s" % (name, i, accum_str(i)))
        yield from asyncio.sleep(i)

@asyncio.coroutine
def slow_operation(future,t):
    yield from asyncio.sleep(t)
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()


tasks = [
    asyncio.Task(put_meter("A", 2)),
    asyncio.Task(put_meter("B", 3)),
    asyncio.Task(put_meter("C", 4)),
    asyncio.Task(put_meter("D", 6))]

if __name__ ==  "__main__":

    # urls to kick
    urls = ["http://xxx.com"]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

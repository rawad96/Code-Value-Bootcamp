# problem 1:

The calls are made one after the other and this wastes a lot of time, so the requests must be sent in parallel, this is possible with asyncio gather.

# problem 2:

Calculating Fibonacci is CPU-bound and will block the event loop, so we should run it in a separate process.

# problem 3:

The time.sleep() is blocking the event loop, so nothing else can run until the sleep is over, so we should use asuncio.sleep() which is not blocking the event loop.

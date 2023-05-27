from threading import Lock
lock = Lock()  # or RLock for reentrant lock

@par
for i in range(100):
    with lock:
        print('only one thread at a time allowed here')
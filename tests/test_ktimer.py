from kott import Kott
from kott.kplugs.ktimer_pool import KTimerPool
from kott.kplugs import ktag
from threading import Timer
import time

Kott.load_kplug("KTag")
Kott.load_kplug("KTimerPool")


def print_me(text):
    print(text)

Kott.set(KTimerPool.create_timer(3, print_me, ["Been called after 3 secs from pool #1"]), pool="pool1")
Kott.set(KTimerPool.create_timer(5, print_me, ["Been called after 5 secs from pool #1"]), pool="pool1")
Kott.set(KTimerPool.create_timer(1, print_me, ["Been called after 1 secs from pool #2"]), pool="pool2")

print("---------- Testing KTimerPool ----------")
t = Kott.find(pool="pool2")
Kott.get(t[0]).start()

Kott.do("kill", pool="pool2")
Kott.do("start", pool="pool1")

alives = Kott.find(pool="pool1", is_alive=True)
while len(alives) > 0:
    print("Still alive:" + str(alives))
    time.sleep(1)
    alives = Kott.find(pool="pool1", is_alive=True)

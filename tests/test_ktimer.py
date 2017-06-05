from kott import Kott
from kott.kplugs.ktimer_pool import KTimerPool
from kott.kplugs import ktag
from threading import Timer
import time


def print_me(text):
    print(text)


def test_load_kplugs():
    Kott.cleanup()
    Kott.load_kplug("KTag")
    Kott.load_kplug("KTimerPool")


def test_timers():
    assert Kott.set(KTimerPool.create_timer(3, print_me, [
        "Been called after 3 secs from pool #1"]), pool="pool1")
    assert Kott.set(KTimerPool.create_timer(5, print_me, [
        "Been called after 5 secs from pool #1"]), pool="pool1")
    assert Kott.set(KTimerPool.create_timer(1, print_me, [
        "Been called after 1 secs from pool #2"]), pool="pool2")


def test_find_and_start_pool():
    print("---------- Testing KTimerPool ----------")
    pool2 = Kott.find(pool="pool2")
    print pool2
    Kott.get(pool2[0]).start()
    assert pool2


def test_kill_on_pool():
    Kott.do("kill", pool="pool2")


def test_start_on_pool():
    Kott.do("start", pool="pool1")


def test_alive_timers():
    while len(Kott.find(pool="pool1", is_alive=True)) > 0:
        print("Still alive:" + str(Kott.find(pool="pool1", is_alive=True)))
        assert Kott.find(pool="pool1", is_alive=True)
        time.sleep(1)

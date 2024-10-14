#!/usr/bin/env python3
""" module that contains a function to measure the runtime of async tasks """
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int):
    """ measure the time it takes for a function to execute"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n

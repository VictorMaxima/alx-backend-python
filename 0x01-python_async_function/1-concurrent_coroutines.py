#!/usr/bin/python3
""" module that calls async concurrent routines"""
import asyncio
mod = __import__('0-basic_async_syntax')


async def wait_n(n: int, max_delay: int):
    """ calls a function n times with the variable argument max_delay"""
    result = []
    tasks = [mod.wait_random(max_delay) for i in range(n)]
    for task in asyncio.as_completed(tasks):
        r = await task
        result.append(r)
    return result

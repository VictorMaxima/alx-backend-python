#!/usr/bin/python3
""" module that calls async concurrent routines"""
import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """ calls a function n times with the variable argument max_delay"""
    result = []
    tasks = [task_wait_random(max_delay) for i in range(n)]
    for task in asyncio.as_completed(tasks):
        r = await task
        result.append(r)
    return result

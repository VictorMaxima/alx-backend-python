#!/usr/bin/python3
""" module for an async funtion that waits for a random period of time"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """ function that waits for a random number of seconds """
    y = random.uniform(0, max_delay)
    await asyncio.sleep(y)
    return y

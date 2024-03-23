#!/usr/bin/env python3
'''The basics of async
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''this waits for a random number of seconds
    '''
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds

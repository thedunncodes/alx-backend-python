#!/usr/bin/env python3
'''to_kv module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a key and its value as a tuple of the key and
    the square of its value.
    '''
    return (k, float(v**2))

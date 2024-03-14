#!/usr/bin/env python3
'''safe_first_element module.
'''
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns first element of lst
    '''
    if lst:
        return lst[0]
    else:
        return None

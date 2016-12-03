# -*- coding: utf-8 -*-
"""docstring."""

import random
import string


def kRandStr(size):
    """docstring."""
    return ''.join(
        random.choice(
            string.ascii_uppercase + string.digits)
        for _ in range(size))

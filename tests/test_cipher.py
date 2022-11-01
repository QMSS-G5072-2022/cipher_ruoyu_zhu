from cipher_rz2562 import cipher_rz2562
import pytest

def test_negative_shift():
    res = cipher_rz2562.cipher('acd',-1)
    assert(res == 'Zbc')
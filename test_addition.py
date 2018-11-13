#!/usr/bin/env python
# -*- coding: utf-8 -*-

from somepackage.helper import give_reverse

def test_add():
    assert 5 == (3+2)
    
def test_give_reverse():
    assert give_reverse('nabin') == 'niban'

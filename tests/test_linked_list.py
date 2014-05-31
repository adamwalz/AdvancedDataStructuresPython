#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from advanced_data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_add(self):
        l = LinkedList()
        l.add(1)

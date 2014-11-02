#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


import unittest
from service.stats import Stats


class TestStats(unittest.TestCase):
    """
    Stats Class Tests
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_single(self):
        """
        single test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        self.assertEqual(single, 225)

    def test_tb(self):
        """
        Total bases test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        tb = Stats.tb(single, 8, 24, 5)
        self.assertEqual(tb, 320)

    def test_rc(self):
        """
        Run created test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        rc = Stats.rc(262, 49, 4, 11, 6, 3, 2, 36, 63, 704, 19, single, 24, 5, 8)
        self.assertEqual(rc, 136.5)

    def test_rc27(self):
        """
        Run created 27 test
        :return:
        """
        # ichiro suzuki(2004)
        single = Stats.single(262, 8, 24, 5)
        rc = Stats.rc(262, 49, 4, 11, 6, 3, 2, 36, 63, 704, 19, single, 24, 5, 8)
        rc27 = Stats.rc27(rc, 704, 262, 2, 3, 11, 6)
        self.assertEqual(rc27, 7.9)

    def test_babip(self):
        """
        BABIP test
        :return:
        """
        # ichiro suzuki(2004)
        babip = Stats.babip(262, 8, 704, 63, 3)
        self.assertEqual(babip, 0.399)

    def test_adam_dunn_b(self):
        """
        adam dunn test(batter)
        :return:
        """
        # adam dunn 2012
        dunn = Stats.adam_dunn_batter(41, 105, 222, 649)
        self.assertEqual(dunn, 56.7)

    def test_adam_dunn_p(self):
        """
        adam dunn test(pitcher)
        :return:
        """
        # hisashi iwakuma 2013
        dunn = Stats.adam_dunn_pitcher(25, 42, 2, 185, 866)
        self.assertEqual(dunn, 29.3)

    def test_pa(self):
        """
        plate appearance test
        :return:
        """
        self.assertEqual(Stats.pa(704, 49, 4, 2, 3), 762)


if __name__ == '__main__':
    unittest.main()


#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import unittest
import sales_taxes

class TestCommonMethods(unittest.TestCase):
    """ Checking First-class functions """
    def test_tax_round(self):
        """ Checking if tax rounding works fine """
        taxes = [2.04, 4.08, 8.16, 9.99, 16.32, 32.64, 512.24]
        rtaxes = [2.05, 4.1, 8.2, 10.0, 16.35, 32.65, 512.25]
        for i in taxes:
            self.assertEqual(sales_taxes.tax_round(i), rtaxes[taxes.index(i)])

    def test_load_order(self):
        """ Simple order loading test """
        order = "data/test_order.txt"
        lo = sales_taxes.load_order(order)
        self.assertEqual(len(lo), 9)

class TestStorageItem(unittest.TestCase):
    """ Storage Item Class test """
    def test_local_tax(self):
        """ Local items tax checking """
        si = sales_taxes.StorageItem('LG0001')
        self.assertEqual(si.tax, 1.9)

    def test_imported_tax(self):
        """ Imported items tax checking """
        si = sales_taxes.StorageItem('IG0004')
        self.assertEqual(si.tax, 0.6)

    def test_no_tax(self):
        """ Check items that are exempt """
        si = sales_taxes.StorageItem('LG0002')
        self.assertEqual(si.tax, 0)

class TestShoppintCart(unittest.TestCase):
    """ Shopping Cart testing """
    def setUp(self):
        self.sc = sales_taxes.ShoppingCart()
        cart_items = [(1, 'LG0001'), (1, 'LG0004'), (1, 'IG0002')]
        for item in cart_items:
            self.sc.add(item[0], item[1])

    def test_sc_tax(self):
        """ Testing tax total in shopping cart """
        self.assertEqual(self.sc.tax(), 6.1)

    def test_sc_subtotal(self):
        """ Testing subtotal calculation """
        self.assertEqual(self.sc.subtotal(), 56.73)

    def test_sc_total(self):
        """ Testing cart total calculation """
        cart_tax, cart_total = self.sc.total()
        self.assertEqual(cart_tax, 6.1)
        self.assertEqual(cart_total, 62.83)


if __name__ == '__main__':
    unittest.main()

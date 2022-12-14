import unittest
import inventory_pb2
import get_book_titles
from unittest.mock import MagicMock
from inventory_client import InventoryClient

class Test(unittest.TestCase):
    def test_mock(self):
        client = InventoryClient("fakeurl")
        client.get_book = MagicMock(return_value=inventory_pb2.Book(
            ISBN="0", title="T0", author="A0", year=2000
        ))
        result = get_book_titles.getBookTitles(client, ["0", "1"])
        self.assertEqual(result, ["T0", "T0"])
        client.get_book.assert_any_call("0")
        client.get_book.assert_any_call("1")

    def test_server(self):
        client = InventoryClient("[::]:50051")
        book1 = {
            "ISBN": "0",
            "title": "T0",
            "author": "A0",
            "year": 2000
        }
        book2 = {
            "ISBN": "1",
            "title": "T1",
            "author": "A1",
            "year": 2001
        }
        client.create_book(book1)
        client.create_book(book2)
        result = get_book_titles.getBookTitles(client, ["0", "1"])

        self.assertEqual(result, ["T0", "T1"])

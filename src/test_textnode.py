import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_when_not_eq(self):
        node = TextNode("This is the first text node", "bold")
        node2 = TextNode("This is the second text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_with_url_defined(self):
        node = TextNode("Text", "bold", "https://localhost:1")
        node2 = TextNode("Text", "bold", "https://localhost:1")
        self.assertEqual(node, node2)

    def test_eq_when_url_is_not_eq(self):
        node = TextNode("Text", "bold", "https://localhost:1")
        node2 = TextNode("Text", "bold", "https://localhost:2")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

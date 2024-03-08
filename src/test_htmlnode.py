import unittest

from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "a.com"}) 
        expected = " href=\"a.com\""
        self.assertEqual(expected, node.props_to_html())

    def test_props_to_html_longer(self):
        node = HTMLNode(tag="a", value="Click me!", props={"class": "greeting", "href": "a.com"}) 
        expected = " class=\"greeting\" href=\"a.com\""
        self.assertEqual(expected, node.props_to_html())

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "a.com"}) 
        expected = f"<{node.tag}> with value: {node.value}, children: {node.children}, and props: {node.props}"
        self.assertEqual(expected, repr(node))

if __name__ == "__main__":
    unittest.main()

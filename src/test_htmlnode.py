import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "a.com"})
        expected = " href=\"a.com\""
        self.assertEqual(expected, node.props_to_html())

    def test_props_to_html_longer(self):
        node = HTMLNode(tag="a", value="Click me!", props={
                        "class": "greeting", "href": "a.com"})
        expected = " class=\"greeting\" href=\"a.com\""
        self.assertEqual(expected, node.props_to_html())

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "a.com"})
        expected = (f"<{node.tag}> with value: {node.value}, "
                    f"children: {node.children}, and props: {node.props}")
        self.assertEqual(expected, repr(node))

    def test_leaf_node(self):
        node = LeafNode(tag="a", value="Click me!", props={
            "class": "test", "href": "a.com"})
        expected = "<a class=\"test\" href=\"a.com\">Click me!</a>"
        self.assertEqual(expected, node.to_html())

    def test_leaf_node_no_tag(self):
        node = LeafNode(None, value="Hello!!")
        expected = "Hello!!"
        self.assertEqual(expected, node.to_html())

    def test_parent_node(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "Italic text")
        children = [child1, child2, child3]

        node = ParentNode("p", children)

        expected = "<p><b>Bold text</b>Normal text<i>Italic text</i></p>"

        self.assertEqual(expected, node.to_html())


if __name__ == "__main__":
    unittest.main()

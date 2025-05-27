import unittest

from HTMLNode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init_default_values(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_tag_and_value(self):
        node = HTMLNode("p", "Hello World")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_all_parameters(self):
        children = [HTMLNode("span", "child")]
        props = {"class": "test", "id": "main"}
        node = HTMLNode("div", "content", children, props)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "content")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_to_html_raises_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_with_none_props(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_with_empty_props(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(props={"class": "container"})
        result = node.props_to_html()
        self.assertEqual(result, 'class:"container"')

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(props={"class": "container", "id": "main", "data-test": "value"})
        result = node.props_to_html()
        # Since dict order is preserved in Python 3.7+, we can test the exact string
        self.assertEqual(result, 'class:"container" id:"main" data-test:"value"')

    def test_props_to_html_with_special_characters(self):
        node = HTMLNode(props={"title": "Hello & Welcome", "data-value": "test's value"})
        result = node.props_to_html()
        self.assertEqual(result, 'title:"Hello & Welcome" data-value:"test\'s value"')

    def test_repr_with_default_values(self):
        node = HTMLNode()
        result = repr(node)
        expected = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(result, expected)

    def test_repr_with_tag_and_value(self):
        node = HTMLNode("p", "Hello")
        result = repr(node)
        expected = "HTMLNode(tag=p, value=Hello, children=None, props=None)"
        self.assertEqual(result, expected)

    def test_repr_with_children(self):
        child = HTMLNode("span", "child")
        node = HTMLNode("div", None, [child])
        result = repr(node)
        expected = f"HTMLNode(tag=div, value=None, children=[{repr(child)}], props=None)"
        self.assertEqual(result, expected)

    def test_repr_with_props(self):
        props = {"class": "test"}
        node = HTMLNode("div", "content", None, props)
        result = repr(node)
        expected = f"HTMLNode(tag=div, value=content, children=None, props={props})"
        self.assertEqual(result, expected)

    def test_repr_with_all_parameters(self):
        children = [HTMLNode("span", "child")]
        props = {"class": "container"}
        node = HTMLNode("div", "content", children, props)
        result = repr(node)
        expected = f"HTMLNode(tag=div, value=content, children={children}, props={props})"
        self.assertEqual(result, expected)
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()
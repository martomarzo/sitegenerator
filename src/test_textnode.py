import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)

    def test_eq_with_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    # def test_not_eq_different_text_type(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.ITALIC)
    #     self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("This is a text node", TextType.LINK, ["https://example.com"])
        node2 = TextNode("This is a text node", TextType.LINK, ["https://different.com"])
        self.assertNotEqual(node, node2)

    # def test_not_eq_url_vs_none(self):
    #     node = TextNode("This is a text node", TextType.LINK, "https://example.com")
    #     node2 = TextNode("This is a text node", TextType.LINK, None)
    #     self.assertNotEqual(node, node2)

    # def test_not_eq_none_vs_url(self):
    #     node = TextNode("This is a text node", TextType.LINK, None)
    #     node2 = TextNode("This is a text node", TextType.LINK, "https://example.com")
    #     self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

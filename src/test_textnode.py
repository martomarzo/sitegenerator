import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    # def test_eq1(self):
    #     node = TextNode("This is NOT text", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.ITALIC)
    #     print("Test 1")
    #     self.assertEqual(node, node2)
        
    # def test_eq2(self):
    #     node = TextNode("This is a text node", TextType.BOLD, "an URL")
    #     node2 = TextNode("This is a text node", TextType.NORMAL)
    #     print("Test 2")
    #     self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

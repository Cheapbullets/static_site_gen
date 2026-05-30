import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This has a `code phrase` inside", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This has a ", TextType.TEXT),
            TextNode("code phrase", TextType.CODE),
            TextNode(" inside", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_bold(self):
        node = TextNode("This has a **bold phrase** inside", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This has a ", TextType.TEXT),
            TextNode("bold phrase", TextType.BOLD),
            TextNode(" inside", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
        
    def test_split_italic(self):
        node = TextNode("This has a _italic phrase_ inside", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This has a ", TextType.TEXT),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" inside", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_pass_through(self):
        node = TextNode("This has a no text type inside", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.TEXT)
        expected = [
            TextNode("This has a no text type inside", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_exception_error(self):
        with self.assertRaises(Exception):
            node = TextNode("This has a `code phrase inside", TextType.TEXT)
            split_nodes_delimiter([node], "`", TextType.CODE)
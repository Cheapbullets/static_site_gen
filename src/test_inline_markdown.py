import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Some text with a [link](https://www.example.com) and maybe another [here](https://www.another.com)"
        )
        self.assertListEqual(
        [
            ("link", "https://www.example.com"),
            ("here", "https://www.another.com")
        ],
        matches
    )
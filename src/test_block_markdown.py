import unittest
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type

class TestSplitNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_block_to_blocktype_header(self):
        md = """# 
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks, BlockType.HEADING
        )


    def test_block_to_blocktype_header2(self):
        md = """###### 
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks, BlockType.HEADING
        )


    def test_block_to_blocktype_header3(self):
        md = """### 
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks, BlockType.HEADING
        )


    def test_block_to_blocktype_code(self):
        md = """```
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
```"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks, BlockType.CODE
        )


    def test_block_to_blocktype_quote(self):
        md = """>
>This is **bolded** paragraph
>
>This is another paragraph with _italic_ text and `code` here
>This is the same paragraph on a new line
>
>- This is a list
>- with items
>"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks, BlockType.QUOTE
        )


    def test_block_to_blocktype_unordered(self):
        md = """- 
- This is **bolded** paragraph
- 
- This is another paragraph with _italic_ text and `code` here
- This is the same paragraph on a new line
- 
- This is a list
- with items
- """
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks, BlockType.UNORDERED_LIST
        )


    def test_block_to_blocktype_ordered(self):
        md = """1. 
2. This is **bolded** paragraph
3. 
4. This is another paragraph with _italic_ text and `code` here
5. This is the same paragraph on a new line
6. 
7. - This is a list
8. - with items
9. """
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks, BlockType.ORDERED_LIST
        )
import unittest
from markdown_to_htmlnode import markdown_to_html_node

class TestSplitNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = md = """
> This is **bolded** paragraph
> text in a p
>tag here
>
> This is another paragraph with _italic_ text and `code` here
> 
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> paragraph text in a p tag here This is another paragraph with <i>italic</i> text and <code>code</code> here</blockquote></div>",
        )

    def test_unordered(self):
        md = """- Item 1
- Item 2
- Item 3"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )

    def test_ordered(self):
        md = """1. Item 1
2. Item 2
3. Item 3"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>",
        )

    def test_heading(self):
        md = """### This is **bolded** Header
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is <b>bolded</b> Header</h3></div>",
        )

    def test_heading2(self):
        md = """# This is **bolded** Header
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is <b>bolded</b> Header</h1></div>",
        )

    def test_heading3(self):
        md = """###### This is **bolded** Header
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is <b>bolded</b> Header</h6></div>",
        )

    def test_heading_error(self):
        with self.assertRaises(Exception):
            md = """
####### This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

            node = markdown_to_html_node(md)
            node.to_html()
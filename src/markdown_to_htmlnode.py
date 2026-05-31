import re
from htmlnode import ParentNode
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type
from textnode import TextNode,TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes


def markdown_to_html_node(markdown):
    final_node = []
    blocked_markdown = markdown_to_blocks(markdown)
    for markdown_block in blocked_markdown:
        block_type = block_to_block_type(markdown_block)
        match block_type:
            case BlockType.PARAGRAPH:
                if re.match(r'^(#)+ ', markdown_block):
                    raise Exception('ERROR: Too many "#" in header')
                clean_children = markdown_block.split("\n")
                children = text_to_children(" ".join(clean_children))
                final_node.append(ParentNode("p", children))
            case BlockType.HEADING:
                if markdown_block.startswith("# "):
                    split_children = markdown_block.split("\n")
                    split_children[0] = split_children[0][2:]
                    children = text_to_children(" ".join(split_children))
                    final_node.append(ParentNode("h1", children))
                elif markdown_block.startswith("## "):
                    split_children = markdown_block.split("\n")
                    split_children[0] = split_children[0][3:]
                    children = text_to_children(" ".join(split_children))
                    final_node.append(ParentNode("h2", children))
                elif markdown_block.startswith("### "):
                    split_children = markdown_block.split("\n")
                    split_children[0] = split_children[0][4:]
                    children = text_to_children(" ".join(split_children))
                    final_node.append(ParentNode("h3", children))
                elif markdown_block.startswith("#### "):
                    split_children = markdown_block.split("\n")
                    split_children[0] = split_children[0][5:]
                    children = text_to_children(" ".join(split_children))
                    final_node.append(ParentNode("h4", children))
                elif markdown_block.startswith("##### "):
                    split_children = markdown_block.split("\n")
                    split_children[0] = split_children[0][6:]
                    children = text_to_children(" ".join(split_children))
                    final_node.append(ParentNode("h5", children))
                elif markdown_block.startswith("###### "):
                    split_children = markdown_block.split("\n")
                    split_children[0] = split_children[0][7:]
                    children = text_to_children(" ".join(split_children))
                    final_node.append(ParentNode("h6", children))
                else:
                    raise Exception('ERROR: Too many "#" in header')
            case BlockType.CODE:
                children = code_to_children(markdown_block[3:-3])
                code_child = ParentNode("code", children)
                final_node.append(ParentNode("pre", [code_child]))
            case BlockType.QUOTE:
                stripped_quote = quote_to_children(markdown_block)
                children = text_to_children(stripped_quote)
                final_node.append(ParentNode("blockquote", children))
            case BlockType.UNORDERED_LIST:
                children = unordered_to_children(markdown_block)
                final_node.append(ParentNode("ul", children))
            case BlockType.ORDERED_LIST:
                children = ordered_to_children(markdown_block)
                final_node.append(ParentNode("ol", children))
            case _:
                raise Exception("ERROR: No block type found")
    return ParentNode("div", final_node)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def code_to_children(text):
    if text.startswith("\n"):
        text = text[1:]
    text_node = TextNode(text, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    return [html_node]

def quote_to_children(text):
    children = []
    split_text = text.split("\n")
    for i in split_text:
        stripped = i.lstrip(">").strip()
        if stripped != "":
            children.append(stripped)
    return " ".join(children)

def unordered_to_children(text):
    children = []
    split_text = text.split("\n")
    for i in split_text:
        clean_text = i[2:]
        inline_children = text_to_children(clean_text)
        children.append(ParentNode("li", inline_children))
    return children

def ordered_to_children(text):
    children = []
    split_text = text.split("\n")
    for i in split_text:
        clean_text = i.lstrip("0123456789")[2:]
        inline_children = text_to_children(clean_text)
        children.append(ParentNode("li", inline_children))
    return children
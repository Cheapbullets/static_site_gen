import re

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = extract_markdown_images(old_node.text)
        if len(sections) == 0:
            new_nodes.append(old_node)
            continue
        current_text = old_node.text
        for image_alt, image_url in sections:
            text_sections = current_text.split(f"![{image_alt}]({image_url})", 1)
            if len(text_sections) % 2 != 0:
                raise ValueError("invalid markdown image")
            split_nodes.append(TextNode(text_sections[0], TextType.TEXT))
            split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            current_text = text_sections[1]
        if current_text != "":
            split_nodes.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = extract_markdown_links(old_node.text)
        if len(sections) == 0:
            new_nodes.append(old_node)
            continue
        current_text = old_node.text
        for link_alt, link_url in sections:
            text_sections = current_text.split(f"[{link_alt}]({link_url})", 1)
            if len(text_sections) % 2 != 0:
                raise ValueError("invalid markdown link")
            split_nodes.append(TextNode(text_sections[0], TextType.TEXT))
            split_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            current_text = text_sections[1]
        if current_text != "":
            split_nodes.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def new_func(new_nodes, old_node):
    new_nodes.append(old_node)
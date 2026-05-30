from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_node = []
    new_string = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
        else:
            new_string = (node.text).split(delimiter)
            if len(new_string) % 2 == 0:
                raise Exception("ERROR: no matching delimiter found")
            for i in range(len(new_string)):
                if i % 2 == 0:
                    if new_string[i] != "":
                        new_node.append(TextNode(new_string[i], TextType.TEXT))
                else:
                    if new_string[i] != "":
                        new_node.append(TextNode(new_string[i], text_type))
    return new_node
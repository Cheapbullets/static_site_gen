from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    split_block = block.split("\n")
    if split_block[0].startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if split_block[0].startswith("```") and split_block[-1].startswith("```"):
        return BlockType.CODE

    check = True
    for i in split_block:
        if not i.startswith(">"):
            check = False
    if check:
        return BlockType.QUOTE
    
    check = True
    for i in split_block:
        if not i.startswith("- "):
            check = False
    if check:
        return BlockType.UNORDERED_LIST
    
    check = True
    for num in range(len(split_block)):
        if not split_block[num].startswith(f"{num + 1}. "):
            check = False
    if check:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
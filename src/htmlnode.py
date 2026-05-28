

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
     
    def to_html(self):
        raise NotImplementedError("ERROR: Did not implement to_html() method")

    def props_to_html(self):
        html_text = ""
        if self.props is not None:
            for i in self.props:
                html_text += f" {i}=\"{self.props[i]}\""
        return html_text
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("ERROR: no value arg was added")
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ERROR: tag arg does not have a value")
        if self.children is None:
            raise ValueError("ERROR: children arg does not have a value")
        else:
            lst = ""
            for i in self.children:
                lst += i.to_html()
            return f"<{self.tag}{self.props_to_html()}>{lst}</{self.tag}>"
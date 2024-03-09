class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # To be overriden by children
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html = ""
        for attribute, value in self.props.items():
            html += f" {attribute}=\"{value}\""
        return html

    def __repr__(self):
        return f"<{self.tag}> with value: {self.value}, children: {self.children}, and props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not value:
            raise ValueError("Leaf nodes require a value")
        if not tag:
            return self.value
        
        props_as_html = self.props_to_html()

        return f"<{tag}{props_as_html}>{self.value}</{tag}>"


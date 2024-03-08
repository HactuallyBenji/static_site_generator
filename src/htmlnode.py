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

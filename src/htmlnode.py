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
        if not self.props:
            return ""
        html = ""
        for attribute, value in self.props.items():
            html += f" {attribute}=\"{value}\""
        return html

    def __repr__(self):
        return (f"<{self.tag}> with value: {self.value}, "
                f"children: {self.children}, and props: {self.props}")


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf nodes require a value")
        if not self.tag:
            return self.value

        props_as_html = self.props_to_html()

        return f"<{self.tag}{props_as_html}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.children:
            raise ValueError("Parent must have children")

        node_and_children_as_html = ""

        node_and_children_as_html += f"<{self.tag}>"
        for child in self.children:
            node_and_children_as_html += child.to_html()
        node_and_children_as_html += f"</{self.tag}>"
        return node_and_children_as_html

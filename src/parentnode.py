from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        
        elif self.children is None:
            raise ValueError("Parent node must have children")

        html = self.props_to_html()
        return (

            f"<{self.tag}{html}>" + "".join(f"{child.to_html()}" for child in self.children) + f"</{self.tag}>"
        )
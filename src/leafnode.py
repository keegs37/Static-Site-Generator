from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        elif self.tag is None:
            return self.value
        else:
            html = self.props_to_html()
            return f"<{self.tag}{html}>{self.value}</{self.tag}>"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props


        )
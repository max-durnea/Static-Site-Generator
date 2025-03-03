class HTMLNode:
	def __init__(self,tag=None,value=None,children=None,props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	def to_html(self):
		raise NotImplementedError("Subclasses must implement this method")
	def props_to_html(self):
		if self.props:
			return " ".join([f'{key}="{value}"' for key,value in self.props.items()])
		else:
			return ""
	def __repr__(self):
		return f"{self.__class__.__name__}({self.tag},{self.value},{self.children},{self.props})"
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have children")
        
        props_html = self.props_to_html()
    
        if props_html:
            return f"<{self.tag} {props_html}>" + "".join([child.to_html() for child in self.children]) + f"</{self.tag}>"
        else:
            return f"<{self.tag}>" + "".join([child.to_html() for child in self.children]) + f"</{self.tag}>"
from enum import Enum

class TextType (Enum):
	NORMAL = "normal"
	BOLD = "bold"
	ITALIC= "italic"
	CODE = "code"
	LINKS = "links"
	IMAGES = "images"

class TextNode:
	def __init__(self,text,text_type,url= None):
		self.text = text
		self.text_type = text_type
		self.url = url
  
	def __eg__(self, other):
		if self == other:
			return True

	def __repr__(self):
		return f"TextNode({self.text},{self.text_type},{self.url})"
	



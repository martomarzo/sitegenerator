from enum import Enum

class TextType (Enum):
	NORMAL = "normal"
	BOLD = "bold"
	ITALIC= "italic"
	CODE = "code"
	LINKS = "links"
	IMAGES = "images"

class TextNode(text,text_type,url=None):
	self.text = text
	self.text_type = text_type.value
	self.url = url


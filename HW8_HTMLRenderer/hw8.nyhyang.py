#!/usr/bin/env python

"""
Python class example.
"""
###############################################################################
#######################   Element and Its Sub Classes   #######################
###############################################################################


class Element(object):
	tag = ""
	ind =  "    "
	attributes = ""
	def __init__(self, content=None, **kwargs):
		"""initialize objects and deal with optinoal atttibutes in the html tags"""

		if not content:
			# if there's no content make an empty list
			self.content = []

		else:
			self.content =  [content]

		for key, value in kwargs.items():
			self.attributes =  self.attributes + " " + key + '="' + value + '"'
			

	def append(self, text):
		self.content.append(text)


	def render(self, file_out, ind = ""):
		"""for rendering the content in html"""
		if self.attributes is not None:
			# include the attribuites in the render
			file_out.write(ind + "<"+self.tag + self.attributes +">\n")
		else:
			file_out.write(ind + "<"+self.tag+">\n")

		# goes through the content to find strings
		for words in self.content:
			if isinstance(words, str):					
				file_out.write(ind + self.ind)
				file_out.write(words)
				file_out.write("\n")

			else:				
				words.render(file_out, ind + self.ind)
		file_out.write(ind)
		file_out.write("</"+self.tag+">\n")
		
class Html(Element):
	tag = "html"
	# overriding render to add doctype
	def render(self, file_out, ind=""):
		file_out.write("<!DOCTYPE html>\n")
		Element.render(self, file_out, ind)


class Head(Element):
	tag ="head"

class Body(Element):
	tag="body"

class P(Element):
	tag ="p"


# Step 3
class OneLineTag(Element):
	# override the render for one line tag
	def render(self, file_out, ind=""):
		file_out.write(ind + "<"+self.tag + self.attributes +">")
		for words in self.content:			
			file_out.write(words)
			file_out.write("</"+self.tag+">\n")


class Title(OneLineTag):
	tag = "title"


# Step 5

class SelfClosingTag(Element):

	def render(self, file_out, ind=""):
		file_out.write(ind + "<" + self.tag + self.attributes + "/>\n")


class Hr(SelfClosingTag):
	tag = "hr"

class Br(SelfClosingTag):
	tag = "br"


# Step 6

class A(OneLineTag):
	tag = "a"

	def __init__(self, link, content):
		Element.__init__(self, content, href=link )


# Step 7

class Ul(Element):
	tag ="ul"


class Li(Element):
	tag = "li"


class H(OneLineTag):
	number= ""
	tag = "h"
	def __init__(self, level, content=None, **kwargs):
		Element.__init__(self, content, **kwargs)
		self.number = str(level)
		self.tag = self.tag + self.number


# Step 8

class Meta(SelfClosingTag):
	tag="meta"



























	

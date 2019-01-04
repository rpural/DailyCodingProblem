#! /usr/bin/env python3

''' Html creation classes

Used to define and display or serve an html web page.
'''


class Tag:
    ''' Tag

            Create a tag definition, providing the tag name, contents, and parameters

            Methods:
                addContent( content ) - Content can be text, or another tag definition
    '''

    def __init__( self, tag, content=None, parameters=None, endtagNeeded=True ):
        self._tagname = tag.lower()
        self._content = []
        self._content.append( content )
        self._endtagNeeded = endtagNeeded
        if parameters != None:
            self._parameters = " " + parameters
        else:
            self._parameters = ""


    def __str__( self ):
        if not self._endtagNeeded and self._content == [None]:
            return "<" + self._tagname + "/>"

        returnString = "<" + self._tagname + self._parameters + ">"

        for c in self._content:
            if c != None:
                returnString += str( c )

        if self._endtagNeeded:
            returnString += "</" + self._tagname + ">"

        return returnString


    def addContent( self, content ):
        self._content.append( content )


class Head(Tag):

    def __init__( self, title, content=None ):
        super().__init__( "head" )
        self._content = []
        self._content.append( Tag( "title", title ))
        self._content.append( content )


class Body(Tag):

    def __init__( self, content=None, parameters=None ):
        super().__init__( "Body", parameters=parameters )

        self.addContent( content )


class Document(Tag):

    def __init__( self, content=None ):
        super().__init__( "html", content )

    def __str__( self ):
        returnString = "<!doctype html>"

        returnString += super().__str__()

        return returnString

if __name__ == "__main__":
    doc = Document()

    header = Head( "Test Page" )
    doc.addContent( header )

    body = Body( parameters="background=white" )
    testTag1 = Tag( "H1", "This is a test" )
    testTag2 = Tag( "p" )
    testTag2.addContent( "This is a paragraph. It contains text." )
    testTag3 = Tag( "br", endtagNeeded=False )
    testTag2.addContent( testTag3 )
    testTag2.addContent( "This is additional text which should appear after a break." )
    testTag4 = Tag( "h2", "This is another test" )

    body.addContent( testTag1 )
    body.addContent( testTag2 )
    doc.addContent( body )

    print(doc)

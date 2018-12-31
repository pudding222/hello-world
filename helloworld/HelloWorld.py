
class HelloWorld(object):

    def __init__(self, environ):
        self.environ = environ
        super(HelloWorld,self).__init__()
        self.headers = {"Content-Type":"text/html"
        }
        
    def getStart(self):
        return "<html>"
        
    def getBody(self):
        return "Hello World" # This should be rendered using Jinja or something else

    def getEnd(self):
        return "</html>"

    def encodeHeaders(self,headers):
        encodedHeaders = []
        for k,values in sorted(headers.items()):
            if not isinstance(values, list):
                values = [values]
            for v in values:
                encodedHeaders.append((k,unicode(v).encode("utf-8")))
        return encodedHeaders


    def main(self):
        content = [self.getStart(),
                   self.getBody(),
                   "Testing",
                   self.getEnd(),
                   ]
        
        
        headers = self.headers
        return ("\n".join(content),self.encodeHeaders(headers))
        
def application(environ, start_response):
    klass = HelloWorld(environ)
    (response, headers) = klass.main()
    start_response("200 OK",headers)
    return [response]
    

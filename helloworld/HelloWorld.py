
class HelloWorld(object):

    def __init__(self, environ):
        self.environ = environ
        super(HelloWorld,self).__init__()
        self.headers = {"Content-Type":"text/html"
        }
        
    def getContent(self):
        return "<html>Hello World</html>" # This should be rendered using Jinja or something else


    def encodeHeaders(self,headers):
        encodedHeaders = []
        for k,values in sorted(headers.items()):
            if not isinstance(values, list):
                values = [values]
            for v in values:
                encodedHeaders.append((k,unicode(v).encode("utf-8")))
        return encodedHeaders


    def main(self):
        content = self.getContent()
        headers = self.headers
        return (content,self.encodedHeaders(headers))
        
def application(environ, start_response):
    klass = HelloWorld(environ)
    (response, headers) = klass.main()
    start_response("200 OK",headers)
    return [response]
    


class HelloWorld(object):

    def __init__(self, environ):
        self.environ = environ
        super(HelloWorld,self).__init__()
        self.headers = []
        

    def getContent(self):
        return "Hello World" # This should be rendered using Jinja or something else

    def main(self):
        content = self.getContent()
        return (content,self.headers)
        
def application(environ, start_response):
    klass = HelloWorld(environ)
    (response, headers) = klass.main()
    start_response("200 OK",headers)
    return [response]
    

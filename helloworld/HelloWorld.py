from flask import Flask
app = Flask(__name__)

class HelloWorld(object):

    def method1(self):
        return "Hello World2"
        
    def main(self):
        return self.method1()
        
@app.route("/")
def hello():
    return HelloWorld().main()

if (__name__ == "__main__"):
    app.run(port = 5000)

from flask import Flask
app=Flask(__name__)
@app.route('/')
def simple_flax():
    return "Hey i am flask server"

@app.route('/hello')
def simple_hello():
    return "Hey i am Hello"

if __name__=='__main__':
    app.run()


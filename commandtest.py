from flask import Flask
import os
app=Flask(__name__)
@app.route('/')
def command():
    os.system('mkdir cyy_test')
    return "OK!"

if __name__ == '__main__':
    app.run()
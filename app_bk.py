from flask import Flask, render_template, make_response
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return('<html><h1>実行結果</h1><p><p><img src="/graph1.png" ></img></html>')

@app.route('/graph1.png')
def graph1():
    fig = plt.figure()
    ax = fig.add_subplot()

    x = np.arange(0, 100, 0.1)
    y = x ** 2

    plt.cla()

    plt.title('Graph')
    plt.legend()
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y)

    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response

# /hello(http://127.0.0.1:5000/hello)にアクセスするとsample.htmlの中身が表示される
@app.route('/hello')
def hello():
    return render_template("sample.html")

if __name__ == '__main__':
    # デバックモードでアプリを起動
    app.run(debug=True)

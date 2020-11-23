from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_login import login_required
from datetime import datetime
from flask import Flask, render_template, make_response
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np

@app.route('/')
@login_required
def show_entries():
    #entries = Entry.scan()
    #entries = sorted(entries, key=lambda x: x.id, reverse=True)
    #return render_template('index.html', entries=entries)
    return render_template('index.html')
    #return('<html><h1>実行結果</h1><p><p><img src="/graph1.png" ></img></html>')

@app.route('/graph1.png')
@login_required
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

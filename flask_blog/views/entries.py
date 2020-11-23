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
import json
import boto3
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import matplotlib.dates as mdates
import os
import base64


de = None

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
    # 【AWS IAM関連情報】
    #  IAMユーザーに割り当てたポリシー
    #   AmazonDynamoDBFullAccess
    #   AWSLambdaDynamoDBExecutionRole
    #  profile名
    #   環境編巣にAWS_DEFAULT_PROFILE, AWS_PROFILEとして定義した。
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table(os.environ['table_name'])
    response = table.scan()

    df = pd.json_normalize(response["Items"])

    # TODO pythonらしい書き方はどんな感じか
    de = df

    # YYYYMMDDHHMMSS形式を日付として認識させる
    df.MeasureDateTime = pd.to_datetime(df.MeasureDateTime)

    # data["value"]はDecimalで入っているが。
    # Decimalは直接表示できないので、floatに変換
    df = df.astype({"value": float})

    # 日付でソートする。戻り値を受け取らないとソートされないので注意
    df = df.sort_values(by='MeasureDateTime')

    fig, ax = plt.subplots()

    # x軸の目盛りは1時間ごとにする（set_major_locatorで目盛りを打つ場所を決める）
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=4))
    # x軸の目盛りの表示形式を設定する（set_major_formatterで目盛りに書く内容を決める）
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d\n%H:%M'))
    # 補助目盛線を付加する
    ax.xaxis.set_minor_locator(mdates.HourLocator())


    plt.plot(df.MeasureDateTime, df.value)
    # ax.plot(df.MeasureDateTime, df.value)というのもある
    plt.title('時間と人数の推移')
    # plt.xlabel('X軸ラベル')
    # plt.ylabel('人数')
    plt.ylabel("人数", rotation=0)
    # 縦書きにする場合
    # ax.set_ylabel("人\n数", rotation=0, va='center')

    plt.grid()
    # 補助目盛は点線にする
    plt.grid(True, which="minor", linestyle="--")
    # 主目盛は実線
    # plt.grid(True, which="major", linestyle="-")

    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()

    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response


# S3の画像をbase64にエンコードして返却
@app.route('/img/<func>')
@login_required
def get_img_from_s3(func):

    s3 = boto3.client('s3')
    bucket_name = os.environ['bucket_name']
    file_path = 'FILE_PATH'
    response = s3.get_object(Bucket=bucket_name, Key=file_path)
    body = response['Body'].read()
    img = base64.b64encode(body)
    return img


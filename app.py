#!/usr/bin/env python3

from flask import Flask, request, render_template
import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json
from kraken import Kraken

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    # input_phone_text = request.form.get("user_phone_input", "")
    input_email_text = request.form.get("user_email_input", "")

    return render_template('echo_user_input.html', email=input_email_text)

@app.route("/graph")
def graph():
    k = Kraken()
    ticker="XXBTZUSD"
    interval=60
    arrMA = [20, 50]

    df = k.get_ohlc(ticker, interval)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["unixtimestap"], 
        y=df["close"]))

    fig.update_layout(autotypenumbers='convert types')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
     
    # Use render_template to pass graphJSON to html
    return render_template('bar.html', graphJSON=graphJSON)
#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_phone_text = request.form.get("user_phone_input", "")
    input_email_text = request.form.get("user_email_input", "")

    return render_template('echo_user_input.html', phone=input_phone_text, email=input_email_text)
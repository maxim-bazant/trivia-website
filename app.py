from flask import Flask, render_template, redirect, request, url_for, flash, session

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
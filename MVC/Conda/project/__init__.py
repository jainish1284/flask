from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = 'abc'

import project.com.controller.RegisterController

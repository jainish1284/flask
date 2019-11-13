from project import app, render_template
from project.com.vo import RegisterVO


@app.route('/')
def index():
    demo = RegisterVO.RegisterVO
    return demo.retrive_info()

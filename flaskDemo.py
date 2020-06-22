from flask import Flask
from flask import request, render_template

app = Flask(__name__)


# 一个路由要与一个函数对应
@app.route('/', methods=['GET', 'POST'])
def index():
    return '''
    <h1>首页</h1>    
    '''

#模板目录可以后添加，一般为templates，通过project structure设置模板路径
#快速换出上下文菜单ALT+ENTER
@app.route('/login', methods=['GET', 'POST'])
def login():
    data = {'title': '登录页面', 'err_msg': '出错信息提示'}
    html = render_template('flaskdemo.html', **data)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18000)

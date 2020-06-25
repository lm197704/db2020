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
    #raise Exception('有异常！！！')
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=18000,
            debug=True,#开启调试模式
            threaded=True,#开启多线程模式
            processes=1#4个进程，默认只有一个进程，注意：theaded、processes不能同时开
            )

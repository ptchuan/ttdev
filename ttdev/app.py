from flask import Flask,render_template

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义路由和视图函数
@app.route('/index')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def hello_world2():
    return render_template('home.html')
# 运行 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
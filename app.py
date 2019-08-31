from flask import Flask
from flask import render_template,request,jsonify
import re
app = Flask(__name__)

@app.route('/ui_calc')
def ui_calc():
    stmt = request.args.get('stmt','NONE')
    if stmt =='NONE':
        print('넘어온 값이 없음')
    else:
        print('넘어온 식:{}'.format(stmt))# 5 + 8
        patt = '[0-9]+'
        op = re.sub(patt,'',stmt)
        print('넘어온 연산자:{}'.format(op))
        nums = stmt.split(op)
        n1 = int(nums[0])
        n2 = int(nums[1])
        if op =='+':result=n1+n2
        elif op == '-': result = n1 - n2
        elif op == '*': result = n1 * n2
        elif op == '/':
            result = n1 / n2

    return jsonify(result = result)
@app.route('/ai_calc')
def ai_calc():
    pass


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move/<path>')
def move(path):
    return render_template('{}.html'.format(path))

if __name__ == '__main__':
    app.run()
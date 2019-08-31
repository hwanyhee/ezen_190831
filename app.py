from flask import Flask
from flask import render_template,request,jsonify
import re
from calculator.controller import  CalculatorController
from cabbage.controller import  CabbageController
app = Flask(__name__)
'''
1.model.py :텐서플로우 모델 생성 코드 및 디렉토리에 모델 저장
2. __init__.py:model.py실행해서 모델 생성
3.controller.py :app에서 받은 데이타를 저장된 모델 불러와서 실행해서 예측
4.app.js:화면에서 값을 받아서 controller생성후 값 전달

'''
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
        elif op == '/': result = n1 / n2

    return jsonify(result = result)


@app.route('/ai_calc',methods=["POST"])
def ai_calc():

    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode=request.form['opcode']

    c = CalculatorController(num1,num2,opcode)
    result =c.calc()
    print('app.py에서 출력한 결과:{}'.format(result))

    return render_template('ai_calc.html',result = int(result))

@app.route('/cabbage',methods=["POST"])
def cabbage():
    #웹에서 사용자 입력값 받기
    avg_temp = request.form['avg_temp']
    min_temp = request.form['min_temp']
    max_temp = request.form['max_temp']
    rain_fall = request.form['rain_fall']
    #컨트롤러 생성시 받은 값 전달후 모델이 예측한 값 받기
    c = CabbageController(avg_temp,min_temp,max_temp,rain_fall)
    result=c.service()

    return render_template('cabbage.html', result=int(result))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move/<path>')
def move(path):
    return render_template('{}.html'.format(path))

if __name__ == '__main__':
    app.run()
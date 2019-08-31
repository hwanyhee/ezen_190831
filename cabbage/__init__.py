#모델실행
'''
1.model.py :텐서플로우 모델 생성 및 디렉토리에 훈련된 모델 저장 코드작성
2. __init__.py:model.py실행해서 모델 생성
3.controller.py :app.py에서 받은 데이타를 저장된 모델 불러와서 실행해서 예측
4.app.py:브라우저 화면에서 값을 받아서 controller생성후 값 전달
'''
from cabbage.model import CabbageModel
import os
if __name__ == '__main__':
    m = CabbageModel()
    m.create_model()

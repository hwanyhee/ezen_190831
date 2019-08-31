import tensorflow as tf

class CalculatorController:
    def __init__(self,num1,num2,opcode):
        self._num1 =num1
        self._num2=num2
        self._opcode=opcode

    def calc(self):
        n1 = self._num1
        n2 = self._num2
        opcode = self._opcode

        print('app.py에서 받은 n1={},n2={},opcode={}'.format(n1,n2,opcode))
        tf.reset_default_graph()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            #저장된 모델 불러오기
            saver = tf.train.import_meta_graph('calculator/saved_add_model/model-1000.meta')
            saver.restore(sess,tf.train.latest_checkpoint('calculator/saved_add_model'))#마지막에 훈련된 체크포인트
            #그래프 얻기
            graph = tf.get_default_graph()
            #그래프에 값 공급하기
            w1=graph.get_tensor_by_name('w1:0')
            w2 = graph.get_tensor_by_name('w2:0')
            feed_dict ={w1:float(n1),w2:float(n2)}
            op_to_restore = graph.get_tensor_by_name('op_add:0')
            #세션으로 실행하기
            result = sess.run(op_to_restore,feed_dict)
            print('텐서가 계산한 결과:{}'.format(result))

        return result
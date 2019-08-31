import tensorflow as tf
import numpy as np
class CabbageController:
    def __init__(self,avg_temp,min_temp,max_temp,rain_fall):
        self._avg_temp=avg_temp
        self._min_temp = min_temp
        self._max_temp = max_temp
        self._rain_fall = rain_fall

    def service(self):
        X = tf.placeholder(tf.float32,shape=[None,4])
        W = tf.Variable(tf.random_normal([4,1]),name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')

        saver = tf.train.Saver()

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            #저장은 상대경로 restore는 프로젝트부터
            saver.restore(sess, 'cabbage/saved_model/saved.ckpt')  # 마지막에 훈련된 체크포인트
            data =[[self._avg_temp,self._min_temp, self._max_temp,self._rain_fall],]#매트릭스에서 첫행만
            arr = np.array(data,dtype=np.float32)
            dict = sess.run(tf.matmul(X,W)+b,{X:arr[0:4]})

            print(dict[0])


        return int(dict[0])
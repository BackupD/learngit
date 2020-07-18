#!/usr/bin/python
# -*- coding=utf-8 -*-
# author:d


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import os
import scipy.misc
from PIL import Image

###获取数据
mnist = input_data.read_data_sets(r'D:/Git/learngit/Data/mnist_dataset',one_hot=True)

#print(mnist.train.images[0,:])

dir_data = r'D:/Git/learngit/Data/mnist_dataset/raw/'
if os.path.exists(dir_data) is False:
    os.makedirs(dir_data)

for i in range(5):
    image_array = mnist.train.images[i,:]
    image_array = image_array * 255
    image_array = image_array.reshape(28,28)
    image_file = dir_data+'mnist_train_%d.jpg' %i
    Image.fromarray(np.uint8(image_array)).save(image_file)
#    scipy.misc.toimage(image_array,cmin=0.0,cmax=1.0).save(image_file)

#输出测试集的标签值，使用softmax
    image_label = mnist.train.labels[i,:]
    label = np.argmax(image_label)
    print('image_train_%d label is : %d' %(i,label))



#使用占位符构建模型先
x = tf.placeholder(tf.float32,[None,784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y_ = tf.placeholder(tf.float32,[None,10])

#y = softmax(x*W+b)
y = tf.nn.softmax(tf.matmul(x,W)+b)

#损失函数
cross_entropy = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)


#上面定义好tensor流，定义好了框架，在session中执行
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for _ in range(1000):
        batch_xs,batch_ys = mnist.train.next_batch(100)
        #初始化变量后，就可以喂数据，真正执行
        sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})

    curr_pre = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
    acc = tf.reduce_mean(tf.cast(curr_pre,tf.float32))
    print(sess.run(acc,feed_dict={x:mnist.test.images,y_:mnist.test.labels}))
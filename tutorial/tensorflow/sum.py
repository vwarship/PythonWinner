import tensorflow as tf

x = tf.constant(1)
y = tf.constant(2)

with tf.Session() as sess:
    print(sess.run(x+y))

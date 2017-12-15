import tensorflow as tf

x = tf.placeholder("float")
y = tf.placeholder("float")

m = tf.multiply(x, y)

with tf.Session() as sess:
    print(sess.run(m, feed_dict={x: 2.2, y: 3}))

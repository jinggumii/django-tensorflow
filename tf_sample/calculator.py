import tensorflow as tf

class Model(object):
    num1 = 0
    num2 = 0

    @property
    def num1(self) -> int: return self.num1

    @num1.setter
    def num1(self, num1): self.num1 = num1

    @property
    def num2(self) -> int: return self.num2

    @num2.setter
    def num2(self, num2): self.num2 = num2

class Service(object):

    this = Model()

    @tf.function
    def plus(self, num1, num2): return tf.add(num1, num2)

    @tf.function
    def minus(self, num1, num2): return tf.subtract(num1, num2)

    @tf.function
    def multiple(self, num1, num2): return tf.mutiply(num1, num2)

    @tf.function
    def div(self, num1, num2): return tf.divide(num1, num2)
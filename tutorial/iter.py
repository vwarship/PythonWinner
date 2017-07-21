import re
import reprlib


text = 'The best way to deploy, operate, and scale MongoDB in the cloud.' \
       'Available on AWS, Azure, and Google Cloud Platform.' \
       'Easily migrate your data to MongoDB Atlas with zero downtime.'

"""第一版 实现了__getitem__"""
class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = re.compile('\w+').findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, reprlib.repr(self.text))


"""第二版 实现了__iter__，采用设计模式的方法"""
class Sentence2(object):
    def __init__(self, text):
        self.text = text
        self.words = re.compile('\w+').findall(text)

    def __iter__(self):
        return Sentence2Iterator(self.words)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, reprlib.repr(self.text))


class Sentence2Iterator(object):
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return word

    def __iter__(self):
        return self


"""第三版 采用生成器的方式实现迭代器"""
class Sentence3(object):
    def __init__(self, text):
        self.text = text
        self.words = re.compile('\w+').findall(text)

    def __iter__(self):
        """使用()来代替下面两行
        for word in self.words:
            yield word
        """
        return (word for word in self.words)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, reprlib.repr(self.text))


"""第四版 iter()"""
class Sentence4(object):
    def __init__(self, text):
        self.text = text
        self.words = re.compile('\w+').findall(text)

    def __iter__(self):
        return iter(self.words)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, reprlib.repr(self.text))


def test_iter(sentence):
    print(iter(sentence))
    print(list(sentence))
    print(sentence)


test_iter(Sentence(text))
test_iter(Sentence2(text))
test_iter(Sentence3(text))
test_iter(Sentence4(text))

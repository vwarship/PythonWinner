import pickle


def save(obj, filename):
    """文件需要使用wb模式，不然出错：TypeError: write() argument must be str, not bytes"""
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)


def read(filename):
    """文件需要使用rb模式，不然出错：UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte"""
    with open(filename, 'rb') as f:
        return pickle.load(f)


d = {'name': 'wjj', 'age': 36}
filename = 'test.obj'
save(d, filename)
print(read(filename))

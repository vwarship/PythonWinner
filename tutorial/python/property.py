class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    # 如果不需要公开设置值就不需要定义
    @grade.setter
    def grade(self, grade):
        if 0 <= grade <= 100:
            self._grade = grade
        else:
            raise ValueError('Grade must be between 0 and 100.')

    # 如果直接返回变量的值就不需要定义
    @grade.getter
    def grade(self):
        if self._grade > 90:
            return 'A'
        elif self._grade > 80:
            return 'B'
        elif self._grade > 70:
            return 'C'
        elif self._grade > 60:
            return 'D'
        else:
            return 'E'

homework = Homework()
homework.grade = 100
print(homework.grade)
class Student(object):

    def __init__(self,name,score):
        # 变量前有两个'_'代表是私有变量
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


bart = Student('Bart Simpson',59)
print(bart.get_score())
bart.set_score(100)
bart.set_score(100)
print(bart.get_score())
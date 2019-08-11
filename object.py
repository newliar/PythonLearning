class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
        
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

        
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
        
        

bart = Student('Bart Simpson',120)
bart.set_score(12)
print(bart.print_score())
print(bart.get_grade())
# print(bart.name)
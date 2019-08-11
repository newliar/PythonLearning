class animal():
    def __init__(self,name,msg):
        self.name=name
        self.msg=msg
    def say(self):
        print("my name is",self.name)
class cat(animal):
    pass
class dog(animal):
    pass

cat_1 = cat("加菲","miao")
cat_1.say()
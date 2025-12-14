class Person(object):
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def ToString(self):
        return "%s is %d years old" % (self.name, self.age)
    @property
    def name(self):
        return self._name

class Student(Person):
    def __init__(self,idStudent, name, age, score):
        super(Student, self).__init__(name, age)
        self.Score = score
        self._idStudent=idStudent

    @property
    def score(self)->float:
       return self.Score
    @score.setter
    def score(self, score:float):
        self.Score = score

    def display_id_student(self):
        return self._idStudent

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

def filter_words(list_words,min_length):
    return list(filter(lambda x :len(x)>=min_length,list_words ))

if __name__ == '__main__':
    #tar1
    listnum = [1,2,3,4,5,6,7,8,9,10]
    list_even= list (filter(lambda x:x%2==0,listnum))
    print(list_even)
    list_even2=[x for x in  listnum if x%2==0  ]
    print(list_even2)
    list_Mull=[x*2 if x%2==0 else x*3 for x in listnum]
    print(list_Mull)

#OOP
    p1=Person("John",20)
    p2=Person("Dan",15)
    print(p1.ToString())
    print(p2.ToString())
    print(p1.name)
    s1=Student("25896314","Yosef",15,100.2)
    print(s1.display_id_student())
    print(s1.name)
    s1.name="Rachel"
    print("the name after: "+s1.name)

#HW FILTER
    words_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
    filtered_words = filter_words(words_list, min_length=5)

    print(filtered_words)
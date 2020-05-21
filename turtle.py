from xml.parsers.expat import ParserCreate


class Student:
    def __init__(self, name=None, age=None, sex=None, score=None):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def __str__(self):
        return "姓名：{0}，年龄：{1}，性别：{2}，成绩：{3}".format(self.name, self.age, self.sex, self.score)


students = []


class MySaxHandler(object):
    def __init__(self):
        self.tag = None
        self.student = None

    def start_element(self, name, attrs):
        # print('start_element: %s---attrs: %s' % (name, str(attrs)))
        self.tag = name
        if name == "student":
            self.student = Student()

    def char_data(self, text):
        # print('content: %s' % text)
        if self.tag == "name":
            self.student.name = text
        if self.tag == "age":
            self.student.age = text
        if self.tag == "sex":
            self.student.sex = text
        if self.tag == "score":
            self.student.score = text

    def end_element(self, name):
        # print('end_element: %s' % name)
        if name == "student":
            students.append(self.student)
            self.student = None
        self.tag = None


with open("students.xml", "r", encoding="utf-8") as stu:
    content = stu.read()

handler = MySaxHandler()
parser = ParserCreate()

parser.StartElementHandler = handler.start_element
parser.CharacterDataHandler = handler.char_data
parser.EndElementHandler = handler.end_element
parser.Parse(content)
for student in students:
    print(student)
class ClassRoom:
    def __init__(self, class_room):
        self.class_room = {'class_num': int(class_room.split()[0]), 'class_letter': class_room.split()[1]}

    def get_name(self):
        return str(self.class_room['class_num']) + ' ' + self.class_room['class_letter']


class Human:
    def __init__(self, surname, name, patronymic, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date

    def get_full_name(self):
        return self.surname + ' ' + self.name[:1] + '.' + self.patronymic[:1] + '.'


class Student(Human):
    def __init__(self, name, surname, patronymic, birth_date, class_room, father, mother):
        Human.__init__(self, name, surname, patronymic, birth_date)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.father.get_full_name(), self.mother.get_full_name()


class Teacher(Human):
    def __init__(self, surname, name, patronymic, birth_date, classes, subject):
        Human.__init__(self, surname, name, patronymic, birth_date)
        self.classes = classes
        self.subject = subject

    def get_classes(self):
        return self.classes


class_rooms = ['3 А', '6 В', '8 Б']
subject = ['Математика', 'Русский язык', 'Литература']
parents = [Human("Кошелев", "Николай", "Игоревич", "05.08.1981"),
           Human("Кошелев", "Мария", "Андреева", "15.08.1971"),
           Human("Бокарев", "Алексей", "Генадьевич", "11.08.1981"),
           Human("Бокарева", "Юлия", "Ивановна", "15.02.1985"),
           Human("Петров", "Владимир", "Александрович", "11.08.1981"),
           Human("Петрова", "Ольга", "Николаевна", "11.08.1981")]
students = [Student("Кошелев", "Святослав", "Николаевич", '10.11.2007', class_rooms[0], parents[2], parents[3]),
            Student("Бокарев", "Святополк", 'Алексеевич', '10.01.207', class_rooms[2], parents[0], parents[1]),
            Student("Петрова", "Анастасия", 'Владимировна', '12.11.2010', class_rooms[1], parents[4], parents[5])]
teachers = [Teacher("Сидоров", "Иван", "Игоревич", "02.06.1981", [class_rooms[0], class_rooms[1]], subject[2]),
            Teacher("Иванов", "Иван", "Александрович", "14.03.1984", [class_rooms[2], class_rooms[1]], subject[1]),
            Teacher("Петров", "Александр", "Александрович", "11.08.1980", [class_rooms[0], class_rooms[2]], subject[0])]

# Получить полный список всех классов школы
st = set([i.get_class_room() for i in students])
print(st)

# Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
cl_room = '3 А'
st_list = [i.get_full_name() for i in students if i.get_class_room() == cl_room]
print(st_list)

# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
student = students[0]
t_list = [i for i in teachers if student.get_class_room() in i.get_classes()]

t_names = [i.get_full_name() for i in t_list]
subj = [subject for i in teachers]
print(student.get_full_name() + ' , ' + student.get_class_room() + ' , ' + ' '.join(
      map(str, t_names)) + ',' + ' '.join(map(str, subj)))

# 4. Узнать ФИО родителей указанного ученика
his_parents = student.get_parents()
print('Родители:', his_parents)
#
## 5. Получить список всех Учителей, преподающих в указанном классе
teach_list = [val.get_full_name() for val in teachers if cl_room in val.get_classes()]
print('Учителя:',teach_list)

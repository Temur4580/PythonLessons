class CourseGroup:
    def __init__(self, student, classmates):
        self.student = student
        self.classmates = classmates

    def __str__(self):
        main_info = f"{self.student.first_name} {self.student.last_name}, {self.student.age} лет, учится на курсе {self.student.course}"
        
        # Создаем список имен сокурсников
        classmates_names = []
        for classmate in self.classmates:
            classmates_names.append(f"{classmate.first_name} {classmate.last_name}")
        
        return f"{main_info} вместе с: {', '.join(classmates_names)}"    
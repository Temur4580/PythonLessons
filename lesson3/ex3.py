from student import Student
from course_group import CourseGroup

# Создаем основного студента
main_student = Student("Иван", "Иванов", 20, 3)

# Создаем список сокурсников
classmates = [
    Student("Петр", "Петров", 21, 3),
    Student("Анна", "Сидорова", 19, 3),
    Student("Мария", "Кузнецова", 22, 3)
]

# Создаем экземпляр группы
group = CourseGroup(main_student, classmates)

# Формируем информацию об основном студенте
main_student_info = f"{main_student.first_name} {main_student.last_name}, {main_student.age} лет, учится на курсе {main_student.course}"

# Формируем список сокурсников
classmates_list = []
for classmate in group.classmates:
    classmates_list.append(f"{classmate.first_name} {classmate.last_name}")

# Выводим информацию о группе
print(f"{main_student_info} вместе с: {', '.join(classmates_list)}")
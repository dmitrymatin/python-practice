from collections import namedtuple


def main():
    Student = namedtuple("Student", ["name", "age", "mark", "city"])
    students = (
        Student("Смирнов Иван", 19, 3, "Владимир"),
        Student("Иванов Петр", 18, 4, "Москва"),
        Student("Кузнецов Сергей", 21, 5, "Владимир"),
        Student("Соколова Василиса",20, 5, "Санкт-Петербург"),
        Student("Лебедев Алексей", 22, 3, "Владимир"),
        Student("Попова Светлана", 19, 4, "Владимир"),
        Student("Волков Александр", 20, 3, "Владимир"),
    )

    good_students(students)


def good_students(students_tuple):
    average_mark = 0
    for student in students_tuple:
        average_mark += student.mark
    average_mark = average_mark / len(students_tuple)

    good_students_list = []
    for student in students_tuple:
        if student.mark >= average_mark:
            good_students_list.append(student.name)

    print(f"Ученики {', '.join(good_students_list)} в этом семестре хорошо учатся!")
    print(f'Средняя оценка: {average_mark}')


if __name__ == "__main__":
    main()

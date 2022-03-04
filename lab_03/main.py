def main():
    employee_count = 16
    employees = {}
    for i in range(employee_count):
        surname = ""
        validSurname = False
        while not validSurname:
            surname = input("surname: ")
            if len(surname) <= 16:
                validSurname = True
        
        name = ""
        validName = False
        while not validName:
            name = input("name: ")
            if len(name) <= 12:
                validName = True

        age = int()
        validAge = False
        while not validAge:
            try:
                age = int(input("age: "))
                validAge = True
            except ValueError as ve:
                print(f"Try again, {ve}")

        conscription = bool()
        validConscription = False
        while not validConscription:
            try:
                conscription = bool(int(input("eligible for conscription: (0 for No, 1 for Yes) ")))
                validConscription = True
            except ValueError as ve:
                print(f"Try again, {ve}")

        employees[i] = {
            "surname": surname,
            "name": name,
            "age": age,
            "conscription": conscription,
        }

    ''' Test code
    employees = {
        1: {
            "surname": "Смирнов",
            "name": "Иван",
            "age": 28,
            "conscription": 0,
        },
        2: {
            "surname": "Иванов",
            "name": "Петр",
            "age": 20,
            "conscription": 0,
        },
        3: {
            "surname": "Кузнецов",
            "name": "Сергей",
            "age": 21,
            "conscription": 0,
        },
        4: {
            "surname": "Соколов",
            "name": "Василий",
            "age": 31,
            "conscription": 0,
        },
        5: {
            "surname": "Попов",
            "name": "Петр",
            "age": 18,
            "conscription": 0,
        },
        6: {
            "surname": "Лебедев",
            "name": "Иван",
            "age": 18,
            "conscription": 0,
        },
        7: {
            "surname": "Козлов",
            "name": "Сергей",
            "age": 19,
            "conscription": 0,
        },
        8: {
            "surname": "Новиков",
            "name": "Василий",
            "age": 39,
            "conscription": 0,
        },
        9: {
            "surname": "Морозов",
            "name": "Иван",
            "age": 23,
            "conscription": 0,
        },
        10: {
            "surname": "Петров",
            "name": "Петр",
            "age": 19,
            "conscription": 0,
        },
        11: {
            "surname": "Волков",
            "name": "Александр",
            "age": 27,
            "conscription": 0,
        },
        12: {
            "surname": "Соловьев",
            "name": "Сергей",
            "age": 60,
            "conscription": 0,
        },
        13: {
            "surname": "Васильев",
            "name": "Иван",
            "age": 24,
            "conscription": 0,
        },
        14: {
            "surname": "Зайцев",
            "name": "Петр",
            "age": 39,
            "conscription": 0,
        },
        15: {
            "surname": "Павлов",
            "name": "Сергей",
            "age": 21,
            "conscription": 0,
        },
        16: {
            "surname": "Семёнов",
            "name": "Василий",
            "age": 31,
            "conscription": 0,
        },
    }
    '''

    youngest = None
    oldest = None
    for k in employees:
        if employees[k]["conscription"] != True:
            continue

        age = employees[k]["age"]
        if youngest == None or age < youngest:
            youngest = age

        if oldest == None or age > oldest:
            oldest = age

    if youngest == None or oldest == None:
        print(
            # Не найдены самый младший или старший сотрудник среди военнообязанных
            f"Could not find the youngest ({youngest}) or the oldest ({oldest}) employees eligible for conscription"
        )
        return

    # Возраст самого младшего военнообязанного сотрудника
    print(f"Youngest eligible for conscription employee age: {youngest}")
    # Возраст самого старшего военнообязанного сотрудника
    print(f"Oldest eligible for conscription employee age: {oldest}")

    ageDiff = oldest - youngest
    # Разница в возрасте между самым младшим и старшим военнообязанными сотрудниками
    print(f"Their age difference: {ageDiff}")

    unconscriptedEmployees = {}
    for k1 in employees:
        if employees[k1]["conscription"] != False:
            continue

        unconscriptedEmployees[k1] = []

        for k2 in employees:
            if k1 == k2:
                continue

            if employees[k2]["conscription"] != False:
                continue

            if k2 in unconscriptedEmployees:
                continue

            currentAgeDiff = abs(employees[k1]["age"] - employees[k2]["age"])
            if currentAgeDiff == ageDiff:
                unconscriptedEmployees[k1].append(k2)

    for k in unconscriptedEmployees.copy():
        if not unconscriptedEmployees[k]:
            del unconscriptedEmployees[k] # TODO: move in the loop above

    print("From uneligible for conscription employees:")
    for k1 in unconscriptedEmployees:
        employee = employees[k1]
        for matchEmployeeId in unconscriptedEmployees[k1]:
            matchEmployee = employees[matchEmployeeId]

            # Фамилии людей среди невоеннообязанных и их разница в возрасте
            print(f"\tEmployee {employee['surname']} and {matchEmployee['surname']} have an age difference {abs(employee['age'] - matchEmployee['age'])}")


if __name__ == "__main__":
    main()
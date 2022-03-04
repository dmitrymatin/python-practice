def main():
    employee_count = 4 #16
    employees = {}
    for i in range(employee_count):
        surname = input("surname: ")  # TODO: validate
        name = input("name: ")
        age = int(input("age: "))  # TODO: validate
        conscription = bool(int(input("eligible for conscription: (0 for No, 1 for Yes) ")))
        employees[i] = {
            "surname": surname,
            "name": name,
            "age": age,
            "conscription": conscription,
        }

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
        print(f"Could not find the youngest ({youngest}) or the oldest ({oldest}) employees eligible for conscription")
        return
    
    print(f"Youngest eligible for conscription employee: {youngest}")
    print(f"Oldest eligible for conscription employee: {oldest}")

    ageDiff = oldest - youngest
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

            if k2 in unconscriptedEmployees: # what about .values()?
                continue

            currentAgeDiff = abs(employees[k1]["age"] - employees[k2]["age"])
            if currentAgeDiff == ageDiff:
                unconscriptedEmployees[k1].append(k2)

    for k in unconscriptedEmployees.copy():
        if not unconscriptedEmployees[k]:
            del unconscriptedEmployees[k]

    print(unconscriptedEmployees)


if __name__ == "__main__":
    main()

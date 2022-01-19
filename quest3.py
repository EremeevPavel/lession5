with open('test_3.txt', encoding='utf-8') as file:
    f_avarage = 0
    file_1 = file.readlines()
    for line in file_1:
        name, salary = line.split()
        salary = float(salary)
        f_avarage += salary
        if salary < 20000:
            print(f'Фамилия:', name, 'Зарплата:', salary, 'RUB')
if len(file_1) > 0:
    f_avarage /= len(file_1)
    print('Средняя зарплата: ', f_avarage, 'RUB')

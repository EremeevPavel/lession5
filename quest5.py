with open('test_5.txt', 'r', encoding='utf-8') as file_test5:
    file_s = file_test5.read()
    print(f'Список чисел в файле: ', file_s)
    res_num = 0

    for i in file_s.split():
        res_num += int(i)
    print(f'Сумма чисел в файле: ', res_num)

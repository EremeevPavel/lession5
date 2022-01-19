
with open('test.txt', 'w', encoding="utf-8") as my_foo:
    my_list = input('Введите текст: \n')
    my_foo.writelines(my_list)


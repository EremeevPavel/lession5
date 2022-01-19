with open('test_6.txt', 'r', encoding='utf-8') as file_1:
    res_dict = {}
    all_read_lines = file_1.readlines()
    for line in all_read_lines:
        if len(line):
            subject = line.split()
            hours_sum = 0
            for hours in subject[1:]:
                if len(hours) > 1:
                    hours_sum += int(hours.split('(')[0])
            res_dict[subject[0]] = hours_sum
    print(res_dict)
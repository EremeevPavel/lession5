
with open("test_2.txt") as read_file:
    all_read_lines = read_file.readlines()
    for num, line in enumerate(all_read_lines):
        el = len(line.split())
        print(f'Всего слов в строке: ', {el})
    print(f"Всего: {len(all_read_lines)} строк(и)\n")
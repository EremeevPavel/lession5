import json

firm_dict = {}
av_dict = {"average_profit": 0}
res_list = [firm_dict, av_dict]
with open("test_7.txt", encoding='utf-8') as read_file:
    i_firm_count = 0
    all_read_lines = read_file.readlines()
    for line in all_read_lines:
        if len(line):
            firm_name, firm_type, firm_revenue, firm_costs = line.split()
        firm_profit = float(firm_revenue) - float(firm_costs)
        firm_dict[firm_name] = firm_profit
        if firm_profit > 0:
            av_dict["average_profit"] += firm_profit
        i_firm_count += 1
    if i_firm_count:
        av_dict["average_profit"] /= i_firm_count
    print(f"{json.dumps(res_list, ensure_ascii=False)}\n")
with open("test_7.json", 'w') as write_file:
    json.dump(res_list, write_file, ensure_ascii=False)

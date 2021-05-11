# 5-7
import json

average_profit = 0
firm_dict = {}
result_list = []
with open("file/file_les_7.txt", "r", encoding="utf8") as f_obj:
    for line in f_obj:
        line_list = line.split()
        firm_name = line_list[0]
        firm_own = line_list[1]
        firm_proceeds = int(line_list[2])
        firm_costs = int(line_list[3])

        firm_profit = firm_proceeds - firm_costs

        if firm_profit >= 0:
            average_profit += firm_profit
            firm_dict[firm_name] = firm_profit
        else:
            average_profit += 0

    average_profit_dict = dict(average_profit=average_profit)

    result_list.append(firm_dict)
    result_list.append(average_profit_dict)

    print(json.dumps(result_list))


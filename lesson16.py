# profit of lemonade is 1.5
# add another day to week 2
# combione 2 lists
# calculate and print how much on th:
# best delattrworst day
# seperate and in total

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
sales.extend(sales_w1)
sales.extend(sales_w2)
#sales = sales_w1 + sales_w2 is another option and probably shorter in this scenario
sales.sort()
worst_day_prof = sales[0] * 1.5
best_day_prof = sales[-1] * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

#OR the end could use min/max

#sales.sort()
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')
# Worst day profit:$ 4.5
# ›Best day profit:$ 63.0
# ›Combined profit:$ 67.5
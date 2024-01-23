# all_bills = ['a,4', 'b,1', 'a,2', 'a,3']

# og_data = []
# duplicate_data = []



# x = ['a,3', 'b,4', 'c,2']
# y = ['a,4', 'b,1', 'a,2', 'a,3', 'c,5', 'a,3']

# for i in range(len(x)):
#     for j in range(len(y)):
#         if x[i].split(',')[0] == y[j].split(',')[0]:
#             x_index = x[i].split(',')[1]
#             y_index = y[j].split(',')[1]
#             total = int(x_index) + int(y_index)
#             x[i] = f"{x[i].split(',')[0]},{total}"






data_list = ['a', 'b', 'c', 'a', 'a', 'b']
main_data = []
duplicate_data = []
seen = set()

for item in data_list:
    if item in seen:
        duplicate_data.append(item)  # Duplicate data
    else:
        seen.add(item)
        main_data.append(item)  # Unique data



print("Main Data:", main_data)
print("Duplicate Data:", duplicate_data)





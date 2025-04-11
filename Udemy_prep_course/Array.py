my_list = [10, 20, 30, 40]

# Lookup
print(my_list[2])  # 30, O(1)

# Search
print(30 in my_list)  # True, O(n)

# Append
my_list.append(50)  # [10, 20, 30, 40, 50], O(1)

# Insert
my_list.insert(1, 99)  # [10, 99, 20, 30, 40, 50], O(n)

# Pop (end)
my_list.pop()  # Removes 50, O(1)

# Pop (index)
my_list.pop(2)  # Removes 20, O(n)

# Remove (by value)
my_list.remove(99)  # Removes 99, O(n)

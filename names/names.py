# use BST from class
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None  # left_LESS_subtree
        self.right = None  # right_GREATER_EQUAL_subtree

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = BinarySearchTree(value)
        else:
            if self.value > value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif self.value <= value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        else:
            if self.value > target:
                if not self.left or self.left.value is None:
                    return False
                elif self.left.value == target:
                    return True
                else:
                    return self.left.contains(target)
            elif self.value < target:
                if not self.right or self.right.value is None:
                    return False
                elif self.right.value == target:
                    return True
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

import time

start_time = time.time()

f = open(r'C:/Users/Todd\Desktop/cs_sprint2/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(r'C:/Users/Todd\Desktop/cs_sprint2/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# print('\nIn the case of nest loops: ')
# print('Complexity = O(n**2)')
# print('The time was: 8.123\n')

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# print('\nIn the case of Binary Search Trees: ')
# print('Complexity = 0(n log n)')
# print('The time was: 0.172\n')

# bst = BinarySearchTree(names_1[0])
# for count, name_1 in enumerate(names_1):
#     if count == 0:
#         continue
#     bst.insert(name_1)

# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

print('\nIn the case of using dict as caches: ')
print('Complexity = O(n)')
print('The time was: 0.008\n')

cache = {}
for name_1 in names_1:
  cache[name_1] = name_1

for name_2 in names_2:
  if name_2 in cache:
      duplicates.append(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

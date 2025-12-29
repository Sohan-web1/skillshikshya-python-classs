# s1 = {3,8,6,8,2,4,6,2,1,8,8}
# print(s1)
# print(type(s1))

# s2 = {"g,s,t,d,t,h,s,q,e,y,u"}
# print(s2)
# print(type(s2))

# empty_set = set()
# print(empty_set)
# print(type(empty_set))

# dup_set = {1,11,2,2,3,3,3,11,1,6,6,7,7,8,8,9,9,10,10,5454,5454}
# print(dup_set)
# print(type(dup_set))

# set = {1,2,3,4,5,6,7,8,9}
# print(set[5])

# empty_set.add(10)
# print(empty_set)

# empty_set.update([1,2,3,4,5,6,7,8,9])
# print(empty_set)

# set = {44,54,1,2,3,4,5,6,7}

# set.remove(2)
# print(set)

# set.discard(3)
# print(set)

# removed = set.pop()
# print("Removed:",removed)
# print(set)

# set1 = {1,2,3,4,5,6,7}
# set2 = {8,9,10,11,12,13,14}

# print("union",set1.union(set2))
# print("intersection",set1.intersection(set2))
# print("difference set2-set1",set2.difference(set1))
# print("difference set1-set2",set1.difference(set2))
# print("symmetric difference:",set1.symmetric_difference(set2))

# print("\n==== 6. mathmatical operation ====")
# print(set1|set2)
# print(set1&set2)
# print(set1 - set2)
# print(set1^set2)

# c={1,2}
# d={1,2,3,4}

# print(c.issubset(d))
# print(d.issuperset(c))
# print(c.isdisjoint({5,6}))

fr = frozenset([1,2,3])
print(fr[0])

print(fr.add(1))
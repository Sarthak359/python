print("\nlist:\n")
l1 = ["sarthak", "shyam", "ram", "abhay"]
l2 = [8, 9, 7, 5, 6, 2, 7]

print("\nsort:")
l1.sort()
l2.sort()
print(l1)
print(l2)

print("\nreverse:")
l1.reverse()
l2.reverse()
print(l1)
print(l2)

print("\nappend:")
l1.append("zack")
l2.append(55)
print(l1)
print(l2)

print("\ninsert:")
l1.insert(0, "ayush")
l2.insert(0, 1)
print(l1)
print(l2)

print("\npop:")
l1.pop(0)
l2.pop(0)
print(l1)
print(l2)

print("\nremove:")
l1.remove("zack")
l2.remove(55)
print(l1)
print(l2)

print("\ncount:")
print(l1.count("sarthak"))
c = l1.copy()
print(c)

print(type(l1), type(l2))


print("\ntuple:\n")

a = (1, 7, 8)
b = ("sarthak",)

print("\ncount:")
print(a.count(1))

print("\nindex:")
print(a.index(1))

print(type(a))

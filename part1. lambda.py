array=[('a',4),('b',2),('c',3)]

def sona(x):
    return x[1]


print(sorted(array, key=sona))  # >>>> [('b', 2), ('c', 3), ('a', 4)]
print(sorted(array, key=lambda x: x[1]))    # >>>> [('b', 2), ('c', 3), ('a', 4)]
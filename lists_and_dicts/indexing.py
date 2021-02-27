import random
a = [random.randint(0, 10) for _ in range(20)]

print(a)
print(a[:100])

first, second, *others = a

print(first)
print(second)
print(others)
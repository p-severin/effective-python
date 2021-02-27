a = 0b10111011
b = 0xc5f

print('Wartość binarna wynosi %d, wartość szesnastkowa wynosi %d' % (a, b))

key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

pantry = [
    ('awokado', 1.25),
    ('banany', 2.5),
    ('wisnie', 15),
]
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (
        i + 1, 
        item.title(), 
        round(count)))

soup = 'pomidorowa'
formatted = 'Dzisiejsza zupa to %(soup)s.' % {'soup': soup}
print(formatted)
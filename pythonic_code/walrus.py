
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5
}

def make_lemonade(count):
    print('making lemonade...')

if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    pass
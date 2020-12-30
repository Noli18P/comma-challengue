def lists(some_list):
    for i in some_list:
        if i == some_list[-1]:
            print(end=('and ') + some_list[-1])
        else:
            print(i, end=(', '))

food = ['apple', 'banana', 'tofu', 'cats']

lists(food)
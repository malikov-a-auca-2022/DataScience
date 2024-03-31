with open('list.txt') as txt:
    txtList = txt.readline()
    list1 = [int(item) for item in txtList.split(sep=', ')]
    print(f'list1 = {list1}')

    sum = sum(list1)
    max = max(list1)
    avg = sum / len(list1)
    print(f'sum_list1: {sum}\n'
          f'avg_list1: {avg}\n'
          f'max_list1: {max}')

    print('Enter the number: ', end='')
    list1.append(int(input()))
    print(f'list1 = {list1}')

    list2 = list1.copy()
    if len(list1) % 2 == 0:
        half_size = len(list2) // 2
        for i in range(half_size):
            list2[i] = list1[i + half_size]
        for i in range(half_size):
            list2[i + half_size] = list1[i] - i - 1
    else:
        half_size = len(list2) // 2 + 1
        for i in range(half_size):
            list2[i] = list1[len(list1) - i - 1]
        for i in range(half_size - 1):
            list2[i + half_size] = list1[i] - i - 1
    print(f'list2 = {list2}')

    print(0 in list1)
    print(0 in list2)

    len_rem = len(list1) % 3
    for i in range(3 - (3 if len_rem == 0 else len_rem)):
        list1.append(0)
        list2.append(0)

    third = len(list1) // 3
    two_thirds = third * 2
    a = list1[0:third]
    b = list1[third:two_thirds]
    c = list1[two_thirds:len(list1)]
    d = list2[0:third]
    e = list2[third:two_thirds]
    f = list2[two_thirds:len(list2)]

    # list_of_lists = [a, b, c, d, e, f]
    print(f'list_of_lists = [{a},\n'
          f'                 {b},\n'
          f'                 {c},\n'
          f'                 {d},\n'
          f'                 {e},\n'
          f'                 {f}]')
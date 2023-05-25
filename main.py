from solution import Solution


if __name__ == '__main__':

    str_arr = input()

    listIn = []
    str_arr = str_arr.split(sep=' ')
    for i in str_arr:
        listIn.append(int(i))

    str_width = input()

    width = int(str_width)

    b = Solution(listIn, width)
    print(b.calculate_max_len())


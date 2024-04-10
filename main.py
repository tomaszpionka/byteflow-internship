a = 1
b = "1"
c = 2


def str_concat_func(string_1, string_2):
    string_final = string_1 + string_2
    print(f"{string_final}\t-\tthis is printed inside of body")
    return string_final


if __name__ == "__main__":
    # print(a+b)
    print(a + int(b))
    print(a + c)  # correct line

    str_1, str_2, str_3 = "a", "b", "c"
    str_concat = str_1 + str_2 + str_3
    print(3 * a)
    print(3 * b)
    print(3 * str_concat)
    str_concat_func(str_1, str_2)

def order(number: str) -> str:
    i = 0
    temp = 0
    listNumber = list(number)
    while(i < len(listNumber)):
        j = 0
        while(j < len(listNumber)):
            if (listNumber[i] > listNumber[j]):
                temp = listNumber[i]
                listNumber[i] = listNumber[j]
                listNumber[j] = temp
            j += 1
        i += 1
    return str(listNumber)


def same_digits(a: int, b: int) -> bool:
    first_number = order(str(a))
    second_number = order(str(b))
    same_digit = False
    i = 0
    if (len(first_number) > len(second_number)):
        while len(first_number) > i:
            j = 0
            while len(second_number) > j:
                if (second_number[j] == first_number[i]):
                    same_digit = True
                else:
                    same_digit = False
                j += 1
            i += 1
            if (not same_digit):
                break
    elif (len(second_number) > len(first_number)):
        while len(second_number) > i:
            j = 0
            while len(first_number) > j:
                if (second_number[i] == first_number[j]):
                    same_digit = True
                else:
                    same_digit = False
                j += 1
            i += 1
            if (not same_digit):
                break
    else:
        same_digit = first_number == second_number
    return same_digit


print(same_digits(37333890, 90837))

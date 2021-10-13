def is_palindrome(x : int):
    '''
    determina daca un numar este palindrom
    :param x: nr. intreg
    :return: 1 daca este palindrom sau False in caz contrar
    '''
    og = 0
    copie = x
    while copie != 0:
        og = og*10 + copie%10
        copie = copie // 10
    if x == og:
        return 1
    else:
        return 0


def lst_all_palindromes(lst):
    '''
    determina daca toate nr. dintr-o lista sunt palindromuri
    :param lst: lista de nr. intregi
    :return: 1, daca toate nr. din lista verifica conditia sau 0 in caz contrar
    '''
    for x in lst:
        if is_palindrome(x) == 0:
            return 0
    return 1


def get_longest_all_palindromes(lst):
    '''
    determina cea mai lunga secventa de numere palindromuri
    :param lst: lista de nr. intregi
    :return: cea mai lunga secventa de numere palindromuri
    '''
    subsecventaM = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst_all_palindromes(lst[i:j + 1]) == 1 and len(lst[i:j + 1]) > len(subsecventaM):
                subsecventaM = lst[i:j+1]

    return subsecventaM

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([]) == []
    assert get_longest_all_palindromes([11, 212, 45, 77]) == [11, 212]
    assert get_longest_all_palindromes([66, 88]) == [66, 88]


def media_lst(lst):
    '''
    determina media numerelor dintr-o lista
    :param lst: o lista de nr. intregi
    :return: media numerelor din lista
    '''
    media = 0
    for x in lst:
        media = media + x
    nr = len(lst)
    return media // nr

def get_longest_average_below(lst, average):
    '''
    determina cea mai lunga secventa de numere a caror medie nu depaseste un nr. dat
    :param lst: lista de nr. intregi
    :param average: nr. intreg
    :return: cea mai lunga secventa de numere a caror medie nu depaseste un nr. dat
    '''
    subsecventaM = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if media_lst(lst[i:j+1]) <= average and len(lst[i:j+1]) > len(subsecventaM):
                subsecventaM = lst[i:j + 1]

    return subsecventaM

def test_get_longest_average_below():
    assert get_longest_average_below([2, 2, 3], 3) == [2,2,3]
    assert get_longest_average_below([1, 1, 1, 1, 1, 1], 2) == [1, 1, 1, 1, 1, 1]
    assert get_longest_average_below([6, 8, 9, 10], 20) == [6, 8, 9, 10]

def list_div_k(lst, k):
    '''
    determina daca toate nr. dintr-o lista sunt divizibile cu k
    :param lst: lista de n r. intregi
    :param k: nr. intrg
    :return: 1 daca toate nr. dintr-o lista sunt divizibile cu k sau 0 in caz contrar
    '''
    for x in lst:
        if x % k != 0:
            return 0
    return 1


def get_longest_div_k(lst, k):
    '''
    determina cea mai lunga subsecventa de numere care sunt divizibile cu un k dat
    :param lst: lista de nr. intregi
    :param k: nr. intreg
    :return: cea mai lunga subsecventa de numere care sunt divizibile cu un k dat
    '''
    subsecventaM = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if list_div_k(lst[i:j + 1], k) == 1 and len(lst[i:j + 1]) > len(subsecventaM):
                subsecventaM = lst[i:j + 1]

    return subsecventaM

def test_get_longest_div_k():
    assert get_longest_div_k([12, 4, 80, 17, 6], 2) == [12, 4, 80]
    assert get_longest_div_k([1, 2, 13, 60, 7], 13) == [13]
    assert get_longest_div_k([12, 4, 81, 17, 6, 44, 12], 2) == [6, 44, 12]


def print_menu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de nr. palindromuri")
    print("3. Afisare cea mai lunga subsecventa de nr. a caror medie nu depaseste un nr. dat")
    print("4. Afisare cea mai lunga subsecventa de nr. care sunt divizibile cu k")
    print("5. Iesire")

def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l

def main():
    test_get_longest_all_palindromes()
    test_get_longest_average_below()
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(get_longest_all_palindromes(l))
        elif optiune == "3":
            average = int(input("Dati average:  "))
            print(get_longest_average_below(l, average))
        elif optiune =="4":
            k = int(input("Dati k: "))
            print(get_longest_div_k(l, k))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Reincercati!")

if __name__ == '__main__':
    main()



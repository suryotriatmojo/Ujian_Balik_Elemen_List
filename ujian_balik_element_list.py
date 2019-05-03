# membuat fungsi balik posisi list
def balikPosisi(a):
    list_balik = []
    for i in range(1, len(a)+1):
        list_balik.append(a[-i])
    return list_balik


print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))
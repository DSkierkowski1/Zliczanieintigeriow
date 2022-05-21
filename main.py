#zliczanie intigerów
# zad2 funkcja zliczająca liczbę liczbę elementów typu int,float i string
# i = 0
# j = len(lista)
# for i in len(lista):
#     if type(lista[i]) is int:
#         liczbaint+=1
#     elif type(lista[i]) is str:
#         liczbastr+=1
#     i+=1
# def coutnType(a_list):
#     liczbaint = 0
#     liczbastr = 0
#     liczbafloat = 0
#     for element in a_list:
#         if isinstance(element, int):
#             liczbaint += 1
#         if isinstance(element, str):
#             liczbastr += 1
#         if isinstance(element, float):
#             liczbafloat +=1
#     print(liczbaint)
#     print(liczbastr)
#     print(liczbafloat)
# lista = [1, 2, 3, 4, "asdasd", "1312311", "13123"]
# coutnType(lista)
#zad3 funkcja zliczająca ilosć stringów w liście
def zliczanieIntigerów(a_list):
    liczbaint = 0
    for element in a_list:
        if isinstance(element, int):
            liczbaint+=1
    print(liczbaint)
lista = [1,2,3,4,5,6,7,234123,12312,3123,123,12,3]
zliczanieIntigerów(lista)








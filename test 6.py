# if else условный оператор
if_rainy = True #дождь будет
if is_rainy:
    print('беру зонт')
    print ('надеть сапоги')
else:
print('не беру зонт')
print('иду гулять')

is_rainy = False #дождя не будет
if is_rainy:
    print('беру зонт')
    print('одеваю сапоги')
else:
    print('не беру зонт')
    print('иду гулять')

    is_rainy = true #дождь будет
    if is_rainy:
        print('беру зонт')
        print('иду гулять')

        is_rainy = false #дождя не будет
        if is-rainy: # ничего распечатано не будет
            print('беру зонт')
            print('иду гулять ')
is_rainy = true #дождь будет
heavy_rain = false #не сильный дождь
if is_rainy:
    if heavy_rain:
        print('беру зонт')
    else:
        print('не беру зонт')
        print('иду гулять')

        is_rainy = true #дождь будет
        heavy_rain = true #сильный дождь
        if is_rainy
            if heavy_rain:
                print('беру зонт')
            else:
                print("беру дождевик")
            else:
            print('не беру зонт')
            print('иду гулять')
print ("Пять больше трех?", 5>3) #true
print ("длина слова 1?", len("hello")==1) #false
print("7 не равно 12?",7!=12) #true
list_= [1,2,3,4,5]
print("в списке есть число 7?", 7 in list ) #false
some_var = None
other_var = None
print(some_var is other_var) #false
# посчитаем пример
example = (2>3) and (2<2) or (1!=5) and (not (5<3) or (3==1))
my_result = false and false or true and (not false or false)
my_result = false and false or true and (true or true)
my_result = false or true
my_result = true
print (example)
print (my_result)
print (example==my_result)
str_1 = 'test'
str_2 = "test"
str_3 = '''test'''
str_4 = """test"""
print (str_1==str_2==str_3==str_4)
print(
    (str_1==str_2)
    and (str_2==str_3)
    and (str_3==str_4)
#плохо
if a>10
    print('а больше 10')
    else:
if a<10
    print ('а меньше 10')
else:
    print ('а равно 10')
    #хорошо
    if a>10:
        print ('а больше 10')
    elif a<10:
        print ('а меньше')
    else:
        print('а равно 10')

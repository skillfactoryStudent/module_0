import numpy
from math import ceil

def game_core_vX(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или 
       увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''


    count = 1
    constant = predict = 50

    
    while number != predict:
        count+=1
        if number > predict: 
            predict = predict + ceil(constant/2**count)
        elif number < predict: 
            predict = predict - ceil(constant/2**count)
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    numpy.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = numpy.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(numpy.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_vX)
"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np


def random_predict(number: int =1) -> int:
    """Рандомно угадываем число

    Args:
         number (int, optional): Загаданное число. Defaults to 1.
         
    Returns:
        int: Число попыток
    """
    
    count = 0
    predict_number = 50 # Предполагаемое число
    max_predict = 101
    min_predict = 0

    
    while True:
        count += 1
                
        if predict_number > number:
            max_predict = predict_number
            predict_number = min_predict + ((max_predict-min_predict) // 2)

        elif predict_number < number:
            min_predict = predict_number
            predict_number = max_predict - ((max_predict-min_predict) // 2)
        
        else:
            break # конец игры, выход из кода
    
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)
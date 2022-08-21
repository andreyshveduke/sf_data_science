import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число . Defaults to 1.

    Returns:
        int: Число попыток за которое было угадано загаданное число 
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,100) # предполагаемое число 
        if number == predict_number:
            break
    #print (f"комп угадал сам себя за {count} попыток")
    return(count)




def effective_predict(number: int=1) -> int:
    """Функция угадывает число меньше чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число поопыток за которое было угадано загаданное число
    """
    
    count = 0
 
    predict_number = 10
    
    while True:
        
        count += 1
  
        if  predict_number == number:
            break
        
        elif predict_number < number:
            predict_number = predict_number + 10 # прибавляем по 10 к каждой попытке , максимум - 10 попыток 
            
        elif predict_number > number:
           
            while True:
                count += 1  
                predict_number -= 1 #уменьшаем по единице до предыдущего десятка , максимум 9 попыток
                if  predict_number == number:
                    break
            break
    #print (f"комп угадал сам себя за {count} попыток")
    return(count)           



def score_game(predict) -> int:
    """Расчитывает среднее  за которое будет найдено  загаданное число от 1 до 100 

    Args:
        predict (_type_): Функция которая угадывает число

    Returns:
        int: среднее из резултьтатов 1000 попыток
    """
    count_ls = []
    random_array = np.random.randint(1,101, size=(1000)) #создаем список из 1000 number
    
    for number in random_array:
        count_ls.append(predict(number)) # добавляем к списку попыток очередной резултьат работы функции 
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)



if __name__ == "__main__":
    score_game( random_predict )
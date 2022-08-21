import numpy as np

def random_predict(number: int=1) -> int:
    """РАндомно угадываем число

    Args:
        number (int, optional): Загаданное число . Defaults to 1.

    Returns:
        int: Число попыток за которое было угадано загаданное число 
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,100) # предполагаемое число 
        if number == predict_number:
            break
    #print (f"комп угадал сам себя за {count} попыток")
    return(count)

#random_predict(50)

def score_game(random_predict) -> int:
    
    count_ls=[]
    random_array= np.random.randint(1,100, size= (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"число попыток = {score}")
    return (score)

if __name__ =="__main__":
    score_game( random_predict )
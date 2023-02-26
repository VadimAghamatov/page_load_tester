from urllib.request import urlopen
import time
import keyboard
from art import tprint


def main():
    
    tprint('Web loading check', font='random')
    url = input("Введите url страницы для проверки её времени загрузки: ")

    while True:
        def get_page_params(url):
            if ("https" or "http") in url:  
                open_this_url = urlopen(url)  
            else:
                open_this_url = urlopen("https://" + url)  
    
            start_time = time.time()  
            open_this_url.read()            
            end_time = time.time()  
            open_this_url.close() 
            time_to_load = end_time - start_time
            page_size = open_this_url.length
            page_info = open_this_url.info()
            return time_to_load, page_size, page_info
        time.sleep(1)   #Время между повторным запросом.


        print(f"\nВремя загрузки страницы {url} составляет {get_page_params(url)[0]:.2} секунды. \
             \nРазмер страницы: {get_page_params(url)[1]} байт. \nИнформация о странице: {get_page_params(url)[2]}")
        
        ###Завершение скрипта###



if __name__ == '__main__':
    main()
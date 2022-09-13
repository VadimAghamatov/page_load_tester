from urllib.request import urlopen
import time
import keyboard
from art import tprint


def main():
    
    tprint('Web loading check', font='bulbhead')
    url = input("Введите url страницы для проверки её времени загрузки: ")

    while True:
        def get_page_load_time(url):
            if ("https" or "http") in url:  
                open_this_url = urlopen(url)  
            else:
                open_this_url = urlopen("https://" + url)  
    
            start_time = time.time()  
            open_this_url.read()  
            end_time = time.time()  
            open_this_url.close() 
            time_to_load = end_time - start_time
 
            return time_to_load
        time.sleep(1)   #Время между повторным запросом.

        print(f"\nВремя загрузки страницы {url} составляет {get_page_load_time(url):.2} секунды.")
        ###Завершение скрипта###



if __name__ == '__main__':
    main()
import enum
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from PIL import Image
import pyautogui as pag
import re
import datetime
import os
from selenium.webdriver.common.keys import Keys

data_fileds = {'Место':'','Дата':'','Время':'','Температура':'','Атмосферное давление':'','Влажность':'','Направление ветра':'','Скорость ветра':'','Осадки, мм':'','Оксид углерода, мг':'','Оксид углерода ПДК':'','Оксид азота, мг':'','Оксид азота ПДК':'','Диоксид азота, мг':'','Диоксид азота ПДК':'','Диоксид серы, мг':'','Диоксид серы ПДК':'','Сероводород, мг':'','Сероводород ПДК':'','Метан, мг':'','Метан ПДК':'','Сумма углеводородов, мг':''}
#skat_list_ID = [20,21,36,40,30,16,4,38,1,43,32,2,22]
skat_list_ID = [22,20]

#список ключей словаря
#--------------------------
#Место
#Дата
#Время
#Температура
#Давление
#Влажность
#Направление ветра
#Скорость ветра
#Осадки, мм
#Оксид углерода, мг/м³
#Оксид углерода ПДК
#Оксид азота, мг/м³
#Оксид азота ПДК
#Диоксид азота, мг/м³
#Диоксид азота ПДК
#Диоксид серы, мг/м³
#Диоксид серы ПДК
#Сероводород, мг/м³
#Сероводород ПДК
#Метан, мг/м³
#Метан ПДК
#Сумма углеводородов, мг/м³
#--------------------------

def get_place_date_time (string):
    string_split = string.split(sep=' ')
    #print (string_split[0])
    data_fileds['Место'] = string_split[0]
    #data_fileds['Дата'] = string_split[1]
    #data_fileds['Время'] = string_split[2]

def get_temperatura (string):
    string_split = string.split(sep=' ')
    data_fileds['Температура'] = string_split[2]

def get_davlenie (string):
    string_split = string.split(sep=' ')
    data_fileds['Атмосферное давление'] = string_split[5]    

def get_vlazhnost (string):
    string_split = string.split(sep=' ')
    data_fileds['Влажность'] = string_split[2]    

def get_napravlenie_vetra (string):
    string_split = string.split(sep=' ')
    data_fileds['Направление ветра'] = string_split[3]    

def get_skorost_vetra (string):
    string_split = string.split(sep=' ')
    data_fileds['Скорость ветра'] = string_split[3]    

def get_osadki (string):
    string_split = string.split(sep=' ')
    data_fileds['Осадки'] = string_split[2]    

def get_oksid_ugleroda (string):
    string_split = string.split(sep=' ')
    data_fileds['Оксид углерода, мг'] = string_split[3]       
    data_fileds['Оксид углерода ПДК'] = string_split[4]   

def get_oksid_azota (string):
    string_split = string.split(sep=' ')
    data_fileds['Оксид азота, мг'] = string_split[3]       
    data_fileds['Оксид азота ПДК'] = string_split[4]    

def get_dioksid_azota (string):
    string_split = string.split(sep=' ')
    data_fileds['Диоксид азота, мг'] = string_split[3]       
    data_fileds['Диоксид азота ПДК'] = string_split[4]  

def get_dioksid_seri (string):
    string_split = string.split(sep=' ')
    data_fileds['Диоксид серы, мг'] = string_split[3]       
    data_fileds['Диоксид серы ПДК'] = string_split[4]   

def get_serovodorod (string):
    string_split = string.split(sep=' ')
    data_fileds['Сероводород, мг'] = string_split[2]       
    data_fileds['Сероводород ПДК'] = string_split[3]       

def get_metan (string):
    string_split = string.split(sep=' ')
    data_fileds['Метан, мг'] = string_split[2]       
    data_fileds['Метан ПДК'] = string_split[3]   

def get_summa_uglevodorodov (string):
    string_split = string.split(sep=' ')
    data_fileds['Сумма углеводородов, мг'] = string_split[3]       

def save_screenshot(string):
    # определяем начальные координаты найденного окна
    location = data.location 
    # получаем размеры найденного окна
    size = data.size 
    # сохраняем скриншот всей страницы
    FullPageScreenshot = now.strftime("%Y-%m-%d-%H-%M-%S")+string+'.png'
    path = 'C:/Python/ecomon/screens/'
    browser.save_screenshot(path+FullPageScreenshot) 
    # вычисляем аргументы для передачи в функцию по обрезке скриншота
    x = location['x'] 
    y = location['y'] 
    w = x + size['width'] 
    h = y + size['height'] 
    # открывает скриншот страницы
    fullImg = Image.open(path+FullPageScreenshot) 
    # вырезаем нужную часть изображения
    cropImg = fullImg.crop((x, y, w, h))
    cropImg.save(path+'_'+FullPageScreenshot) 
    os.remove('C:/Python/ecomon/screens/'+FullPageScreenshot)  

#------------------------------------------------------------------------------------



'''
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'none'
browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome('chromedriver.exe')
browser.set_window_size(1200, 1000)
#browser.get('http://ecomap.orb.ru/map/')
'''



browser = webdriver.Chrome('chromedriver.exe')
browser.set_window_size(1200, 1000)
browser.get("http://ecomap.orb.ru/map/")
#browser.set_page_load_timeout(2)
#browser.get('http://ecomap.orb.ru/map/')
#sleep(2)
#browser.refresh()
#browser.set_page_load_timeout(2)
#browser.find_element_by_tag_name("html").send_keys(Keys.F5)


# create action chain object
#action = ActionChains(browser)
# perform the operation
#action.key_down(Keys.CONTROL).send_keys('F5').key_up(Keys.CONTROL).perform()

#browser.refresh()
#browser.get('http://ecomap.orb.ru/map/')



# получаем все div'ы со СКАТами
#element = browser.find_elements_by_xpath ("//*[@id='map-107868']/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/div[4]/div")


'''
#установка видимого курсора над выбранным элементом
canvas_x_offset = browser.execute_script("return window.screenX + (window.outerWidth - window.innerWidth) / 2 - window.scrollX;")
canvas_y_offset = browser.execute_script("return window.screenY + (window.outerHeight - window.innerHeight) - window.scrollY;")
pag.moveTo (element[1].rect["x"] + canvas_x_offset + element[1].rect["width"] / 2,
                    element[1].rect["y"] + canvas_y_offset + element[1].rect["height"] / 2)

pag.scroll(500)
element[1].click()
sleep(2)
btn_close = browser.find_element_by_class_name("v-window-closebox")
btn_close.click()
sleep(2)
pag.scroll(-500)
'''

#element[0].click()

#sleep(5)

#получаю все данные с открывшегося поста
#data = browser.find_element_by_xpath ('//*[@id="map-107868-overlays"]/div[2]/div')
#перевожу полученные данные в текст
#sensor_data = str(data.text)
#sensor_data_string = sensor_data.splitlines()
#pag.moveTo(600,500)
#pag.scroll(-500)
#print (sensor_data)

#текущее время
now = datetime.datetime.now()

for q in skat_list_ID:    
    try:
        #обработка Красный Коммунар-2, клик по координатам из-за близкого расположения рядом 2 СКАТов на карте
        if q == 20:
            sleep(3)
            ActionChains(browser).move_by_offset(645, 330).click().perform()
            #ActionChains(browser).move_by_offset(645, 330).click().perform()
            sleep(3)

            # ищем открывшееся после клика окно с данными о ПДК
            data = browser.find_element_by_xpath('//*[@id="map-107868-overlays"]/div[2]/div') 
           
            save_screenshot('kk2')

            btn_close = browser.find_element_by_class_name("v-window-closebox")
            btn_close.click()
            sleep(1)

            browser.refresh()

        else:
            #-------------------------------------------------------------------
            #поиск следующей точки и ее центрирование на экране
            sleep(2)
            element = browser.find_elements_by_xpath ("//*[@id='map-107868']/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/div[4]/div")
            pag.moveTo(600,500)
            pag.scroll(-500)
            sleep(2)
            #установка видимого курсора над выбранным элементом
            canvas_x_offset = browser.execute_script("return window.screenX + (window.outerWidth - window.innerWidth) / 2 - window.scrollX;")
            canvas_y_offset = browser.execute_script("return window.screenY + (window.outerHeight - window.innerHeight) - window.scrollY;")
            pag.moveTo (element[q].rect["x"] + canvas_x_offset + element[q].rect["width"] / 2,
                        element[q].rect["y"] + canvas_y_offset + element[q].rect["height"] / 2)
            sleep(1)
            pag.scroll(700)
            sleep(2)
            element[q].click()
            sleep(2)
            #-------------------------------------------------------------------
            

            #обработка информации со СКАТа

            #ищем открывшееся после клика окно с данными о ПДК
            data = browser.find_element_by_xpath('//*[@id="map-107868-overlays"]/div[2]/div') 

            #перевожу полученные данные в текст
            sensor_data = str(data.text)
            sensor_data_string = sensor_data.splitlines()

            #получаю название населенного пункта, дату и время
            get_place_date_time (sensor_data_string[0])

            save_screenshot(data_fileds['Место'])

            btn_close = browser.find_element_by_class_name("v-window-closebox")
            btn_close.click()
            #sleep(1)
        
        


        
        #навожусь на элемент
        #hover = ActionChains(browser).move_to_element(element[q]).perform()
        #sleep(2)
        #нужно переместить физический курсор на элемент и сделать скролл
        #browser.execute_script("arguments[0].scrollIntoView(true);", element[q])
    


        #кликаю по элементу
        #ActionChains(browser).click(element[q]).perform()
        #sleep(2)
        #btn_close = browser.find_element_by_class_name("v-window-closebox")
        #sleep(2)
        #btn_close.click()
       

        sleep(1)
        browser.refresh()


        #pag.click(x, y)
        #element[q].click()
        #data = browser.find_element_by_xpath ('//*[@id="map-107868-overlays"]/div[2]/div')
        #sensor_data = str(data.text)
        #sensor_data_string = sensor_data.splitlines()
        #get_place_date_time (sensor_data_string[0])           
        #btn_close = browser.find_element_by_class_name("v-window-closebox")
        #btn_close.click()
        



    except Exception as ex:
        print ('Исключение: '+ str(ex))
        browser.refresh()
    
        

browser.quit()


#---------------------------------------------
# ID СКАТов на карте
'''
0	10 линия
1	9 января
2	Бердянка
3	Береговой
4	Бородинск
5	Городище
6	Дедуровка
7	Джеланды
8	Зубочистенка-1
9	Зубочистенка-2
10	Ивановка
11	Илек
12	Илекская
13	Караваева роща
14	Караванный
15	Карачи
16	Комарова
17	Котова 40
18	Котова 46а
19	Краснохолм
20	Красный коммунар-1
21	Красный коммунар-2
22	Лабужского
23	Луговое
24	Марьино
25	Медногорск
26	Нижняя Павловка
27	Никольское
28	Новотроицк
29	Паника
30	Переволоцкий
31	Пруды
32	Пугачевский
33	Пустобаево
34	Рычковка
35	Самородово
36	Сорочинск
37	Станиславского
38	Старица
39	Татищево
40	Ташла
41	Узловой
42	Чкалов
43	Школьная
44	Шуваловка
'''
#---------------------------------------------
#показывает координаты курсора

# На первом этапе импортируем модули  pyautogui, time. Также напечатаем напоминание пользователю, о возможности выхода из программы нажав CTRL-C
import pyautogui
import time
from selenium import webdriver
print("Press CTRL-C to quit")

'''
Для постоянного вывода текущих координат из mouse.position() можно использовать бесконечный цикл. А для кода завершающего программу нужно будет перехватить исключение KeyboardInterrupt, которое возникает всякий раз, когда пользователь нажимает CTRL-C.
Если этого не сделать то try/exept отобразит уродливую строку сообщения об ошибке.
И чтобы обработать цикл заключим его в  оператор try '''

try:
    while True:
      # получение текущих координат
      x, y = pyautogui.position()
      # метод str(x) превращает число в строку а rjust(4) сдвигает его на четыре позиции вправо
      positionStr = 'X:'+ str(x).rjust(4) +'  Y:'+ str(y).rjust(4)
      # end предотвращает добавление символа новой строки,  без  этого старые координаты удалить не получится
      print(positionStr, end = '')
     
      # escape-символ \ b стирает конец строки и чтобы удалить всю строку умножаем его на длину строки
      print('\b'*len(positionStr), end = '', flush = True)
     
      # для предотвращения мигания при выполнении цикла используем засыпание
      time.sleep(0.01)



# Когда пользователь нажимает CTRL-C, выполнение программы переходит к разделу except и # Done будет напечатан с новой строки

except KeyboardInterrupt:
    print('\nDone')
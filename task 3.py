# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023

@author: workk



Упражнение 61. Действительный номерной знак машины?
(Решено. 28 строк)
Допустим, в  нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв, следом за которыми шли три цифры. 
После того как все возможные номера были использованы, формат был изменен на четыре цифры, предшествующие трем заглавным буквам.

Напишите программу, запрашивающую у пользователя номерной знак машины и оповещающую о том, для какого формата подходит данная последовательность символов: 
для старого или нового. Если введенная последовательность не соответствует ни одному из двух форматов, укажите 
это в сообщении
"""

import re

def task3(num):
  old_num = re.match(r'\w\w\w\d\d\d', num)
  new_num = re.match(r'\d\d\d\d\w\w\w', num)
  print("\n\ntest\n")  
  if old_num != None and old_num.group(0) == num:
    print('the old format of the vehicle number')
  elif new_num != None and new_num.group(0) == num:
    print('new vehicle number format')
  else:
    print('unavailable vehicle number format')

task3('AAA343')
task3('AFN34342')
task3('DFBGD344343')
task3('7512UTR')

task3('1234afa')
task3('afa123')
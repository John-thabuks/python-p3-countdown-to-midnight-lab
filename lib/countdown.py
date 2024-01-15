# your code goes here!
# def countdown(number):
#     while(number >= 1):
#         print(f"{number} SECOND(S)!")
#         number = number -1
#     print(f'{number} SECOND(S)!')
import time

def countdown(number):
  num = 1
  while (number >= num):
    print(f"{number} SECOND(S)!")
    number = number - 1
  print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
  num = 1
  while (number >= num):
    print(f"{number} SECOND(S)!")
    time.sleep(1)
    number = number - 1
  print("HAPPY NEW YEAR!")
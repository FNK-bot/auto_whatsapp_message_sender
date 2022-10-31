import pyautogui as pg
import pyfiglet
import time
import pandas as pd

result = pyfiglet.figlet_format(" Auto messsage sender by  FNK ")

print(result)
value = input("enter message you want to sent \n")

msg = int(input("enter how many messages \n"))

intr= int(input("enter the time(seconds) required for switching task \n better less than 50\n"))

print("the message is : " + value)
print("total messges :"+ str(msg))
print("please place youre pointer where do you want to send and press enter")
print("starting sending messages ")


time.sleep(intr)
for i in range(msg):
    pg.write(value)
    pg.press("enter")

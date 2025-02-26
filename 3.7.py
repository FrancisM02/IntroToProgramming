# (Random character) Write a program that displays a random uppercase letter using the time.time() function
import time

currenttime = int(time.time())

random_num = currenttime % 26 # 26 because there are 26 letters in the alphabet
random_letter = chr(65 + random_num)

print(f"A Random Uppercase Letter: {random_letter}")
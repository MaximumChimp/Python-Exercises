#PROBLEM:  Create a countdown timer that starts from a given number and counts down to zero using a while loop.
#PURPOSE: In this exercise, you will learn about loop termination logic and time delay management. Knowing how to control the flow of your code in real time is important for making animations, game loops, or automated scripts.

import time
def simple_count_down(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n -1
    print("Blast off!")

simple_count_down(5)
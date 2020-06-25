import math
def main():
    P = float(input("initial acct balance"))
    r = float(input("annual interest rate"))
    R = r / 100.0
    t = int(input("number of years"))
    for n in range (0,t+1):
        print((P * R * n) + P) 
main()
#!/usr/bin/env python3

def triple(num):
    return num*3

def square(num):
    return num**2

def main():
    for i in range(1, 11):
        t=triple(i)
        s=square(i)
        if t < s:
            break
        print("triple({:.0f})=={:.0f} square({:.0f})=={:.0f}".format(i, t, i, s))
        

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, prepend):
        self.pre = prepend
    
    def write(self, text):
        print(f"{self.pre}{text}")

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def extract_numbers(s):
    numerot = []
    for sana in s.split():
        try:
            numerot.append(int(sana))
        except Exception as e:
            try:
                numerot.append(float(sana))
            except Exception as e:
                print(e)
    return numerot

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()

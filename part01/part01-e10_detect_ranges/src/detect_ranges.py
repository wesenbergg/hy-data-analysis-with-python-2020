#!/usr/bin/env python3

def detect_ranges(L):
    list = []
    output = []
    list.extend(L)
    list.sort()

    start=list[0]
    interval=False
    for i in range(0, len(list) - 1):
        if(list[i] - list[i+1] == -1):
            if not interval:
                start=list[i]
                interval = True
            end=list[i+1]+1
        else:
            if interval:
                interval = not interval
                output.append((start, end))
            else:
                output.append(list[i])
    
    #Lisää viimeinen jäsen
    output.append((start, end)) if interval else output.append(list[-1])
    return output

def main():
    L = [-4, -2, 0, 2]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

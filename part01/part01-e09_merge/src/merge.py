#!/usr/bin/env python3

def merge(L1, L2):
    list=[]
    list.extend(L1)
    for i in range(len(L2)):
        added=False
        for j in range(len(list)):
            if(L2[i] < list[j]):
                list.insert(j, L2[i])
                added = True
                break
        if not added: list.append(L2[i])

    return list

def main():
    merge([-99, -96, -80, -64, -51, -31, -30, -26, -9, -4, 12, 19, 25, 28, 49, 62, 63, 82, 87, 90], [-53, -43, -40, -13, 1, 16, 29, 37, 69, 93])
    #print(out)
    #print(len(out))

if __name__ == "__main__":
    main()

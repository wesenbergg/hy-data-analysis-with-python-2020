#!/usr/bin/env python3

# Tehtävä 4
# def main():
#     for i in range(1, 6):
#         for j in range(1,6):
#             if i+j==5:
#                 print("("+str(i)+","+str(j)+")")

def main():
    print("\n".join(f"({a},{b})"
    for a in range(1,7)
    for b in range(1,7)
    if a+b==5))

if __name__ == "__main__":
    main()

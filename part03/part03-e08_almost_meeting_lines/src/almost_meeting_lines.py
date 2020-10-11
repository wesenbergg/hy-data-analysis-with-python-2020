#!/usr/bin/python3

import numpy as np

def almost_meeting_lines(a1, b1, a2, b2): # ax + b = cy => b = -ax + cy
    A = np.array([ [-a1, 1], [-a2, 1] ])
    b = np.array([b1, b2])

    try:
        x, y = np.linalg.solve(A, b) #Lines meeting
        return [(x, y), True]
    except Exception as e:
        x, y = np.linalg.lstsq(A, b)[0] #Lines not meeting
        return [(x, y), False]

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()

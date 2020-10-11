#!/usr/bin/env python3

import pandas as pd
import numpy as np

def cities():
    return pd.DataFrame(
        [
            {'Population': 643272, "Total area": 715.48},
            {'Population': 279044, "Total area": 528.03},
            {'Population': 231853, "Total area": 689.59},
            {'Population': 223027, "Total area": 240.35},
            {'Population': 201810, "Total area": 3817.52}
        ], index=["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"])
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()

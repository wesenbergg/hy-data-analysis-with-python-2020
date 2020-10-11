# Enter you module contents here
from math import sqrt

# print("The docstring is:", hypothenuse.__doc__)
# print("The docstring is:", area.__doc__)
__version__ = '1.0.0'
__author__ = 'Bee-oo-än-gee-oo'
__doc__ = '012345666789'

def hypothenuse(sivu1, sivu2):
  "This function multiplies its argument by two."
  return sqrt(sivu1**2+sivu2**2)

def area(w, h):
  "This function multiplies its argument by two."
  return w*h/2
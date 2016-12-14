#!/usr/bin/env python
import numpy as np
from structures import Data


def main():
    measured_data = Data()
    print measured_data
    a = 1.0
    b = 2.0
    c = 3.0
    measured_data.append_data(a, b, c)
    print measured_data




if __name__ == '__main__':
    main()

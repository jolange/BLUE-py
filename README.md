Python package implementing the Best Linear Unbiased Estimate (BLUE) method for combining measurements.

Copyright 2018 Johannes Lange (see LICENSE.txt)


## BLUE method

A description of the BLUE method as implemented in this package can be found in

- L. Lyons, D. Gibaut and P. Clifford,
  "How to Combine Correlated Estimates of a Single Physical Quantity",
  Nucl. Instrum. Meth. A 270 (1988) 110,
  doi:10.1016/0168-9002(88)90018-6.

- A. Valassi,
  "Combining correlated measurements of several different physical quantities",
  Nucl. Instrum. Meth. A 500 (2003) 391,
  doi:10.1016/S0168-9002(03)00329-2.

## Installation
- requires python3 and numpy
- install release version using pip:
```
pip install blue_combine
```

- install development version from git:
```
git clone git@github.com:jolange/BLUE-py.git
pip install [-e] .
```

## Usage
- the examples directory contains different usage possibilities
- `basic_blue.py`: basic usage of the BLUE class (example in Nucl. Instrum. Meth. A 270 (1988) 110)
- `from_correlation_matrix.py`: use uncertainties and correlation matrix as input
- `uncertainty_sources.py`: specify different uncertainty sources with individual correlations
- `reduced_correlations.py`: use the "reduced correlations" option
  (reduce a 100% correlation to rho = sigma_X/sigma_Y, assuming sigma_X <= sigma_Y)

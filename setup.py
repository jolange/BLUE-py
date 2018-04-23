from setuptools import setup


long_desc = """A description of the BLUE method as implemented in this package can be found in

- L. Lyons, D. Gibaut and P. Clifford,
  "How to Combine Correlated Estimates of a Single Physical Quantity",
  Nucl. Instrum. Meth. A 270 (1988) 110,
  doi:10.1016/0168-9002(88)90018-6.

- A. Valassi,
  "Combining correlated measurements of several different physical quantities",
  Nucl. Instrum. Meth. A 500 (2003) 391,
  doi:10.1016/S0168-9002(03)00329-2.
"""

setup(name='blue_combine',
      version='0.1.dev1',
      description='Python package for the Best Linear Unbiased Estimate (BLUE) method',
      long_description=long_desc,
      url='https://github.com/jolange/BLUE-py',
      author='Johannes Lange',
      license='GPL-3.0',
      packages=['blue_combine'],
      python_requires='>=3',
      install_requires=['numpy'])

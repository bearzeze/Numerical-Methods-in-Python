# **Numerical Methods With Python**

## Basic and most used numerical methods coded in Python 3.11

Numerical methods and code are divided in sections with numerous most popular methods for each section. Also there are Python built-in methods shown as well for each section:

1. **Finding Roots of High-Degree Equations**
2. **Interpolation and Approximation**
3. **Differentiation**
4. **Integration**
5. **Systems of Linear Equations**
6. **Ordinary Differential Equations**

## **How To Use Code**
Fork and download if you and as you like.

## **Sections Descripiton**
Every section provides user defined code of the known methods as well as Python built-in functions.
<br />
<br />

### **Section 1 - Roots of High Degree Equations**
There are code for the known algorithms of finding the roots of the high-degree equations:
* Simple Iteration method
* Newton-Raphson method
* Bisection method
* False Position (Regula Falsi) method
* Secant method

There are also Python built-in methods from the SciPy module,shown with example:

* `root()`
* `fsolve()`
* `bisect()`
* `newton()`

You will need first to install scipy module:

`pip install scipy`

And afterwards import methods in the .py file:

`from scipy import root, fsolve, bisect, newton`
<br />
<br />

### **Section 2 - Interpolation and Curve Fitting**
There are code for the known algorithms of interpolating and approximating given data with the desired curves. 

For interpolation method which are introduced and coded are:
* Linear Interpolation
* Lagrange Interpolation
* Newton Interpolation

For approximation there are next methods:
* Linear Regression
* Polynomial Approximation

There are also Python built-in methods from the SciPy module, shown with example:

* `interp1d()`
* `lagrange()`
* `linregress()`
* `curve_fit()`

You will need first to install scipy module:

`pip install scipy`

And afterwards import methods for interpolation and curve fitting:

`from scipy.interpolate import interp1d, lagrange`

`from scipy.stats import linregress`

`from scipy.optimize import curve_fit`
<br />
<br />

### **Section 3 - Numerical Differentiation**
There are code for the three methods for numerical differentiations:
* Forward Method
* Central Method
* Backward Method

 Emphasis is on the best of these three - central method where plotting of first and second derivative is also shown 

There is also Python built-in methods from the SciPy module, shown with example:

* `derivative()`

You will need first to install scipy module:

`pip install scipy`

And afterwards import methods for interpolation and curve fitting:

`from scipy.misc import derivative`
<br />
<br />



## **Needs To Be Done**
- Curve fitting with various functions: exponential, logarithmic, and so on
- Numerical methods for solving systems of non-linear equations
- Numerical methods for solving systems of ordinary differential equations

## **Contact**
Any information, bugs or questions can be sent on the e-mail adress: i.zejd@hotmail.com


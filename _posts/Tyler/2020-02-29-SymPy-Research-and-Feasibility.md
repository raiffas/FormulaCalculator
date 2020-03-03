---
layout: post
title: "SymPy Research and Feasibility"
Tyler: Tyler
---

[SymPy](https://www.sympy.org/en/index.html "SymPy Homepage") is a symbolic mathematics library for Python. More formally, it is a computer algebra system or CAS, which allows for symbolic manipulation of mathematical expressions. For this project, such a system sounds like it could be used, as a key element of the project involves taking formulas and iteratively deriving new variables from a given set of data. This blog will detail the currently know needs of the software project, and how SymPy is able to address these issues.

# Solving Equations
SymPy is able to handle all the equations we need for the project. It is capable of handling even calculus problems, let alone the mainly algebraic equations we have for this project. It also includes methods to substitute values for variables in expressions and solve for a given variable symbolically. With the use of symbolic manipulation, this mean the system is able to give exact answers if necessary, rather than solely numerical ones.

# Storing Equations as Text
SymPy also includes methods to build expressions and equations from text. There exist several formats, though the two most common and appealing ones are the native Pytho/SymPy syntax or LaTeX. From the documentation, the former is more stable and reliable, so it seems more likely to be chosen in the final design of the project. Either way, this proves to be a viable method of storing the equations in a human-editable manner, which is a key part in our modular design.

# Numerical Evaluation
Beyond symbolic evaluation. SymPy offers a method `lambdify`, which can translate the expressions into functions. This could be useful if the speed of computation becomes too slow, as this will greatly speed up numerical evaluation. From personal testing and observation of the amount of data in question, this may not be necessary, but useful just in case.

# Conclusion
Overall, SymPy look like a solid library to leverage in this project. By using this, we should be able to greatly simplify the construction of the formula solving system.

Word count total: 939

---
layout: post
title: "Sprint 1 Progress"
Tyler: Tyler
---

I've not made much progress code-wise since the beginning of the sprint. I anticipated this, given the timing of the sprint with midterms. I've figured out what I can do for the problem of converting equation text from `a = b` to `Eq(a, b)`. As I suspected, regular expressions will allow me to both verify that a line of the text file is formatted in the standard form for an equation, and then obtain the text of the left and right hand side in order to reformat them into proper SymPy notation. The regular expression I've chosen for this is the following.

> (.\*)=(.\*)

The only issue might be with extraneous whitespace, but that can be easily resolved by using built-in methods for strings to strip of white space. The only other issue, which I still haven't found a good solution for, is a method for sanitizing inputs. If I recall correctly, the parse uses 'eval()', which can run arbitrary code without some method of sanitizing input. If I can find a solution for this, that would be great, but otherwise I'll need to note this during the maintenance phase of the project. This wouldn't be a set-back though, since Mike has no intention of pushing this code immediately into production. At worst, this would just become another project for another CS499 team in the future.

Regardless, the parts I have should be easy enough to implement after midterm week, especially since I would have about four and a half days to work on it without anything else going on. I've also got to look into the 'unittest' Python module to see how creating testing code for that works and how well I can automate unit testing.

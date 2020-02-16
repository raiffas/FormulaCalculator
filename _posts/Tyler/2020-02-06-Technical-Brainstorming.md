---
layout: post
title: "Technical Brainstorming"
Tyler: Tyler
---

Today was the meeting with Mike Flamm, the owner and buisness contact for DeltaV. After talking with him about the new software system, I along with the rest of my team got a clear idea about the function of the software system and its requriement. There appeared to be two main components to it:

1. Extracting Tables from a PDF file
1. Solving formulas given some input variables 

# PDF extraction
Tables can appear in text-based PDFs, but it's usually not easy to transfer that data from the pdf to something easier to work with, say, a CSV. However, each car manufacturer has differences in how the report PDf is formatted and the units some measurements use.

Mike suggested that perhaps that this might be applicable to use AI. However, I've been able to find software packages that seem to achieve this without needing AI. The most prominent one I've seen so far is [Tabula](https://tabula.technology/).

# Formulas
Given all the data from the user, there needs to be some method to determine based on a given set of formulas whether any new variable can be derived. Of course, these new variables could lead to more solvable variables in turn. 

In thinking about this problem, two methods of discovering all the possible variables that can be solved are
1. Iterativly check unused formulas if something can be solved until no unusued formulas can be used
1. Analyze the formulas once and build a "road map" from formula to formula, then solve each formula in order
For simplicity, I'm thinking that the former method would be the direction we would head in, if for no other reason than it seems to be the easier to implement and/or is the first algorithm to come to mind. 

As to how to implement these formulas, perhaps a software module for symbolic mathematics would work, since we would need to be able to rearrange formulas. Something like [SymPy](https://www.sympy.org/en/index.html) 
would seem to work.

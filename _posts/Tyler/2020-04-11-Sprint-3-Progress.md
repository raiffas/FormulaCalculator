---
layout: post
title: "Sprint 3 Progress"
Tyler: Tyler
---

Unfortunately, due to time constraints, I've been unable to perform as much code development as I would have preferred. Currently, I have re-designed the configuration files to be encoded using YAML rather than using my own "parser" to read them in. In the long run this will be a much more maintainable solution, as adding more information to the configuration files will require little/no changes to the code that loads it in. This will allow for our and future teams to focus our attention more on operations that use and manipulate that information. There might need to additional code to confirm the structure of the objects derived from the YAML files, but that is out of scope for this sprint and will likely need to be left to another team.

As for the equation solver code itself, I do have a rough idea of the methods I need to implement. I'll start with some pseudo-code for the overall `calc_equations` method and then expand the logic and methods out as needed. One challenge I would like to tackle is the cleanly handling units. I vaguely recall that SymPy has something on units and maybe even dimensional analysis, but I need to investigate how I can use that to help with unit checking and deriving. If possible, I would like it if I could somehow format the units into the equations and let the solving process derive the units for the final answer. I'll have to investigate and see.

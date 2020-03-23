---
layout: post
title: End of First Sprint
author: Raiffa
Raiffa: Raiffa
---

In the past couple of weeks we have finished our architecture assignment, held our first sprint planning meeting, and had the majority of our first sprint! Our first sprint has gone on a little longer than scheduled, but the last half of it did overlap spring break so that was expected.

In this sprint I was tasked with user stories that focused on the storage and presentation of data. Both ended up being more complicated than I had anticipated.

For the presentation of results user story, I focused on how we generate PDFs given our desired data. The goal here was basically generate a PDF using python. I ended up needing to write a wrapper for a python latex generating library called pylatex. This was to create an easier interface for the library that can be easily integrated into our code. Learning latex as a part of the first assignment really came in handy because I would not have easily or quickly came up with that solution if it weren't for my familiarity with latex.

For the storage of data user story, I was working on developing the class for our crashPkg--our solution to standardize the data that would go into a crash data processing project. I ran into a block as the design we had discussed in reference to the crashPkg and the overall architecture was not in depth enough. During our team meeting today, we hammered out exactly how this package would be used as a way to standardize how information is saved on a machine but also how information is passed throughout the system. Before our next sprint planning meeting Tyler and I will be working on refactoring our design to reflect this change. 

---
layout: blog_onlyCameron
permalink: /CameronBlog/
title: "Cameron's Blog"
---

# Welcome to Cameron's Blog!
Running word count: 2,046 (including meeting blog posts)

### About Me
I am a senior at the University of Kentucky studying Computer Science and minoring in Mathematics. I plan to graduate in December 2020. My main interests in the Computer Science field is Web Development, and I have 3 years of professional experience in this field so far. I am also looking into branching out into other fields. I have been working at Computer Services Inc. doing Web Development since the summer after my freshman year.

### Crash Pulse Formula Calculator with Delta V Innovations
#### An Overview
Delta V Innovations asked us to create an application that could take in a Crash Data Report (CDR), in the form of a PDF, and extract the information in it and run calculations on that data. A Crash Data Report contains information about a crash between 1 or more vehicles. The report has information such as whether or not the driver's seatbelt was on, velocity of the car over the last 5 seconds before the crash and the next 5 seconds immediately after, whether or not the airbag was deployed, whether or not the brakes were used, etc. As you can see, they are going to be pretty lengthy. The reports also vary significantly by manufacturer. It is only required by law that the manufacturers have a way to collect this information, but now how to organize the Crash Data Report. Currently, they have to input all this data and run the calculations by hand, which takes a lot of time and is prone to user error. They are looking for as little user input as possible as well as a fast run time. The only user input that should be needed is to specify the PDF to be extracted and other information about the vehicles involved in the crash.

#### Tabula
As the project has moved forward, I chose to tackle the task of extracting the data from the Crash Data Reports. I believe it was Tyler that first mentions Tabula.py to us. After a quick search, I too, thought that this library would be perfect. In the Tabula.py library there is a method "read_pdf()" that will simply extract all tables from a PDf and return the data as a list of DataFrames, which is an object from the pandas library. Each DataFrame in the list will contain all of the information in one table of the PDF and thus the entire list has all the information from the PDF. However, when it comes to filtering out this data to the rest of the application, it gets a little tricky becuase the pandas library is very picky. In one case, I realized that the DataFrame.filer method will not be able to find data labelled "Time" if the data in the table is labelled "time". The difference in capitalization here makes all the difference.

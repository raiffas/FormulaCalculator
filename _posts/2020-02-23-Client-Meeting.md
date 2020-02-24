---
layout: post
Meeting: Honor
author: Honor
---

We set up this meeting for Mike to walk us through the thought process a user might take if they didn't have access to our application. Only Kyra and Honor attended the meeting over Zoom. The others were unavailable due to things like illness and family obligations. Honor recorded the meeting and uploaded it to the Team Drive.

Mike walked us through a Crash Data Retrieval (CDR) report, a PDF of vehicle and accelerometer data. The format of each CDR report is specific to each vehicle's make and year. He went through almost every piece of data and explained for what he used it. Mike informed us that he needed to get some paperwork finished before he could release some example CDR reports to the team. 

One thing that became abundantly clear during this meeting was that graphical representations are prefered, whether a bird's eye view of the car position over the course of the event or a simple graph. Additionally, we pushed him for what calculations were absolutely necessary for the application. He said,
<ol>
  <li>Align data to a 0 time.</li>
  <li>Calculate total Delta V using whatever equations necessary.</li>
  <li>Calculate data conversions between g-forces and mph. If both are provided in CDR report do conversions anyway to test accuracy of the provided data.</li>
</ol>

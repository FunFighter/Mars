# Mars

This application was a fun one (help me).

## Web Scraping.
The scraping script goes out and pulls different data from the following sources.
https://mars.nasa.gov/news/
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
https://twitter.com/marswxreport?lang=en

To get around the roadblock of scraping blockers I used Splinter to open a browser to emulate a "real person".

## Database
For the task at hand I felt the best tool for the job would be a MongoDB since while they might be the same topic the data being pulled had different forums.

## Flask
Went with flask but would have just preferred to do this in Node.js (since node is pretty cute).
Only thing of note is the try except to make sure that there is data in the data base to load on the first pull.

# GTF Assignment Software

*Copyright 2017 Joshua Kerr*

# Design

## Front-end

User stories:
- Be greeted by an explanation of how to use the software
- Upload a cvs file with proper information
- Be notified if the cvs file is erroneous
- Adjust how important seniority really is (slider bar?)
- Adjust whether or not the system prioritizes acceptable assignments for everyone (that is, "everyone gets at least 3rd choice")
- Display resulting assignments
- "Disallow" a given pairing and have things recalculated
- Print out results

Interface:
- Initial
	- Introductory explanation with in-depth information if needed
	- Upload system
	- Display of assignments
	- Print function
- Additional features
	- Seniority weight selection (is this really necessary?)
	- Checkbox or something to allow "make everyone somewhat happy"
	- Button or something to prohibit each pairing (or two dropdowns to define a pairing as prohibited?) pairing as prohibited?)
	- Recalculation option

## Back-end

Initial
- Read uploaded file into a database
- Run the algorithm on the database
- Produce a new database consisting of the proper assignments

For additional features
- Adjust algorithm to use options
- Keep track of prohibited pairings

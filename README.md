# Data-mining
Project 1, Week 1


Prompts used to troubleshoot:

Gemini AI Prompts: 
An overview of the prompts and questions you used to refine the web scraping script for this assignment follows, categorized by the problems we solved.
1. Script Logic & Loops
•	"Can I not use the first loop? I want all the names through all pages?"
•	"I meant the code with the first loop limiting to first 4 pages of each position"
•	"I do not want to limit to the first hour pages even though I only need 1000 tuples minimum."
•	"well when running code, it did not stop count on QB and went beyond number on site. what is the error"
•	"only reaching 424 tuples, not getting all players, looks like stopping on second page, not writing any on second page"
2. HTML Parsing & Data Extraction
•	"why did you add in the code and cols[0].find("a"):"
•	"this is what each players source code looks like..."
•	"I actually do not care about the data columns after team"
•	"the tags for the code tr, tag too many things that my output is chaotic. I think I need to resort back to the tag tr class_=tableclmhder."
•	"well I do not see a change in the code that fixes the chaos. But I have an idea, what if, at the end of cols = row.find_all("td") we added a class=sort1..."
3. File Management & Output
•	"well the actual output only put out QBmaybe it overwrote old data"
•	"ok, so three issues. it's partly working but saving in a rogue spot. The second issue is it prints the first player 3 times. the last issue is it only prints the first page..."
4. Error Handling
•	"anything wrong with this code..."
•	"getting an error..."



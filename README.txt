Use hotel_data_test.csv and hotel_test.json in the data folder are used for designing right now.

Since we are changing dataset layout right now, I will update it at final. 

Then use hotel_reviews.csv and hotel_reviews.json when everything is done! ( it is too large!!!)

--------------------------------------------
TODO:
Edits to the data file:
- change "stayed _ nights" to just an integer for nights stayed
- remove leading and trailing whitespace in some cells

Visualizations to make:
- geographic visualization -C
 -*Add color gradient depending on avg review score
 - Add interaction
  - hotel/review information on hover/click
-*D3 bar graphs
 - avg&total reviews vs room type
 - avg&total reviews vs nationality
 - avg&total reviews vs trip type
 - avg&total reviews vs review month
- (possibly) calendar vis of avg revew score per day/week
- (possibly) D3 pie charts, word clouds (check proposed solutions)
 - Get .txt of list of words, not including stopwords

Other:
- Figure out how to implement filtering of the data to apply to all of the visualizations

*After making visualizations:
Write-ups/presentation:
- link and test live demo in presentation
- backup snapshots of demo in case live demo issues
- (optional) Evaluation
---------------------------------------------
List of stopwords from https://gist.github.com/sebleier/554280
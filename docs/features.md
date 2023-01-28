# Feature List <br/>

<ul>
<li> Users can query the API for a list of the edits made to an article, by a user, or across Wikipedia for some category of edits (vandalism, etc.).
<li> Users can filter this list by:
	<ul>
	<li> time period of edits
	<li> keyword in edit contents
	<li> edits made only by anonymous or identifiable users	
	<li> Wikipedia client used to make edit (iOS, visual, etc.)
	<li> type of edit (vandalism, "shouting", date of birth/death change, etc.)
	<li> potentially more filters (Wikipedia has a broad variety of <a href="https://en.wikipedia.org/wiki/Special:Tags">tags</a> for edits)
	</ul>
<li> Users can query for the oldest or most recent edit of an article.
<li> User can include a request for a visualization of their query's response:
	<ul>
	<li> Different types of chart produced for different types of query, e.x. pie chart for which articles a user has contributed to, heat map for how frequently certain sections of an article are edited.
	<li> User can specify parameters for the visualization e.x. how many slices for a histogram of an article's edit frequency, etc.).
	</ul>
</ul>

# Minimum Viable Product<br/>

<ul>
<li> Queries for history of edits to an article, with filters for: 
	<ul>
	<li> time period
	<li> keyword
	<li> type of edit (vandalism, punctuation, etc.)
	</ul>
<li> Queries for history of edits by a user, with filters for: 
	<ul>
	<li> time period
	<li> keyword
	</ul>
</ul>

# Structure <br/>

<ul>
<li> API
<ul>
<li> app.py - define endpoints
<li> articleHistory.py 
<li> userHistory.py
<li> tagHistory.py
</ul>
<li> Scraper
<ul>
<li> historyScraper.py
<li> diffScraper.py
</ul>
<li> Data
<ul>
<li> article.py
<li> edit.py
<li> user.py
</ul>
</ul>


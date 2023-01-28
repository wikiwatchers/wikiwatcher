# Feature List <br/>

<ul>
<li> get edit list for article or user edit history
<li> filter list by time period and/or keyword/tags
<li> view oldest edit
<li> view newest edit
<li> filter by tags with specific options- client used to make edit, what type of edit
<li> compare anonymous contributions versus known users
<li> visualize data (server side)- client specifies how many slices/bars in histogram
<li> how frequently is a page or section of a page edited
<li> color html text according to how frequently a page is edited
<li> how often is a page undone or reverted to a previous version
</ul>

# Minimum Viable Product<br/>

<ul>
<li> scrapes Wikipedia 
<li> returns a list of edits for article's edit history
<li> returns a list of edits for user's edit history
<li> for both article and user edit history, client can specify a time period and/or keyword
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


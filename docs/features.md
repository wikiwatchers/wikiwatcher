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
<li> Users can query for the oldest or most recent version of an article, or any version at any arbitrary point in time.
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
<li> Queries for the oldest or newest version of an article, or for the version of that article at any arbitrary point in time.
</ul>

# Structure <br/>
<ul>
/
<ul>
    <li>README.md</li>
    <li>app.py</li>
    <li>// several hidden/config files and directories e.x. .gitignore, .pylintrc</li>
    <li>src/</li>
	<ul>
        <li>revision.py</li>
            // contains revision class, acts as data structure for properties of a single revision & has methods for getting the content of that revision (has to query its article; does not store the diff in as a property of the class), potentially more methods
        <li>revisionHistory.py</li>
            // base class for storing a collection of revisions, with a filter method; contains overlapping filter implementation of subclasses below
        <li>articleHistory.py</li>
            // stores collection of revisions for an article, with filter method implementation specific to articleHistory (is there any?)
        <li>userHistory.py</li>
            // stores collection of revisions for a user, with filter method implementation specific to userHistory (is there any?)
	</ul>
    <li>tests/</li>
	<ul>
        <li>test_revision.py</li> // details of contents tbd
        <li>test_revisionHistory.py</li> // details of contents tbd
        <li>test_articleHistory.py</li> // details of contents tbd
        <li>test_userHistory.py</li> // details of contents tbd
	</ul>
    <li>docs/</li>
	<ul>
        <li>devNotes.txt</li>
        <li>features.md</li>
        <li>requirements.txt</li>
	</ul>
    <li>venv/</li>
	<ul>
        // in .gitignore; contains per-development-environment files
	</ul>
</ul>
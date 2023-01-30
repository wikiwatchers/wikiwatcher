# WikiWatcher <br /><br />

<p>WikiWatcher is an API for retrieving data about the history of edits made to an article or by a user on Wikipedia. Proposed endpoints include: </p>
<ol>
	<li>/articleEdits - accepts a filter for the name of an article</li>
	<li>/userEdits - accepts a filter for the ID of a user</li>
	<li>/articleVersion - accepts a filter for the name of an article</li>
</ol>
<p>Endpoints 1 and 2 can additionally be filtered by:</p>
 <ul>
	<li> time period of edits (begin & end datetime)
	<li> keyword in edit contents
	<li> type of edit (vandalism, "shouting", date of birth/death change, etc.)
</ul>
<p>Endpoint 3 accepts only one additional filter - a datetime specifying the version of the article to return to the client. Values before the inception of wikipedia or the target article will return the first ever published version of that article, while values after the present will return the most recent version.</p>
<p>The API is intended to facilitate or ease the development of applications which use the data it returns. We hope to include a small toy example of such an application once the API itself is in a client-ready state.</p>

<p>The API will be implemented using the Flask framework for Python which has a concise, powerful interface for implementing REST APIs and companion web applications.</p>

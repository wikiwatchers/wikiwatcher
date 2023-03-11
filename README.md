# WikiWatcher <br /><br />

<p>WikiWatcher is an API for retrieving data about the history of edits made to an article or by a user on Wikipedia.  Endpoints include: </p>
<ol>
	<li>/articleHistory/title - Requires the title of an article.</li>
		By default, retrieves the 10 most recent revisions made to the article.<br/>
		Optional parameters:
		<ul>
		<li>startyear</li>
		<li>startmonth</li>
		<li>startday</li>
		<li>starthour</li>
		<li>startminute</li>
		<li>startsecond</li>
		startx parameters specify a date and time which acts as a lower bound on the timestamp of retrieved revisions.
		Date/time parameters, if specified, must be supported by all units of time greater than themselves - <br/>
		i.e. if a month is specified, a year must also be specified. If a day is specified, a month and a year must also be specified, etc.<br/>
		Times are to be specified in 24-hour format, from hour 0 through 23.<br/>
		If a time is before the first existing edit or after the present day, the nearest valid date/time will be used.
		<li>endyear</li>
		<li>endmonth</li>
		<li>endday</li>
		<li>endhour</li>
		<li>endminute</li>
		<li>endsecond</li>
		endx parameters specify a date and time which acts as an upper bound on the timestamp of retrieved revisions.
		These date/time parameters follow the same specificity rules as those in the endpoints above.
		<li>tags</li>
		tags should be a comma-separated bracket-enclosed list of strings matching wikipedia's available reviser-applied tags for revisions.<br/>
		Single tags still require the enclosing brackets.

		view a comprehensive list of available tags <a href=https://en.wikipedia.org/wiki/Special:Tags>here</a>.
		<li>user - retrieve only revisions to the specified article which were created by this username.</li>
		<li>keyword - retrieve only revisions whose contents contain this keyword.</li>
		</ul>
	<br/>
	<li>/userHistory/user - Requires the username of a wikipedia editor.</li>
		By default, retrieves the 10 most recent revisions made by the user.<br/>
		Optional parameters:
		<ul>
		<li>startyear</li>
		<li>startmonth</li>
		<li>startday</li>
		<li>starthour</li>
		<li>startminute</li>
		<li>startsecond</li>
		See above for an explanation of startx parameters.
		These date/time parameters follow the same specificity rules as those in the endpoints above.
		<li>endyear</li>
		<li>endmonth</li>
		<li>endday</li>
		<li>endhour</li>
		<li>endminute</li>
		<li>endsecond</li>
		See above for an explanation of endx parameters.
		These date/time parameters follow the same specificity rules as those in the endpoints above.
		<li>tags</li>
		See above for an explanation of the tags parameter.
		<li>title - retrieve only revisions created by the specified user made to this article.</li>
		<li>keyword - retrieve only revisions whose contents contain this keyword.</li>
		</ul>
	<br/>
	<li>/getRevision/title - Requires the title of an article.</li>
		By default, retrieves the state of the article after the most recent revision.
		Optional parameters:
		<ul>
		<li>year</li>
		<li>month</li>
		<li>day</li>
		<li>hour</li>
		<li>minute</li>
		<li>second</li>
		</ul>
		These parameters specify that the API should retrieve the state of the article at this date/time.
		These date/time parameters follow the same specificity rules as those in the endpoints above.<br/>
	<br/>
	<li>/compareRevisions/title - Requires the title of an article.</li>
		Parameters:
		<ul>
		At least a startyear and an endyear are required. Remaining parameters are optional.
		<li>startyear</li>
		<li>startmonth</li>
		<li>startday</li>
		<li>starthour</li>
		<li>startminute</li>
		<li>startsecond</li>
		Here, startx parameters specify the first revision to compare.
		These date/time parameters follow the same specificity rules as those in the endpoints above.
		<li>endyear</li>
		<li>endmonth</li>
		<li>endday</li>
		<li>endhour</li>
		<li>endminute</li>
		<li>endsecond</li>
		Here, endx parameters specify the second revision to compare the first to.<br/>
		These date/time parameters follow the same specificity rules as those in the endpoints above.
		</ul>
</ol>

<p>The API is intended to facilitate or ease the development of applications which use the data it returns. We hope to include a small toy example of such an application once the API itself is in a client-ready state, or potentially a graphical frontend which will replace this page (while still making the readme accessible through a separate link/url).</p>

<p>The API is implemented using the Flask framework for Python.</p>

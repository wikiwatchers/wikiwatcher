# WikiWatcher <br /><br />

an API for retrieving information about the edit history of a page
on Wikipedia. Proposed endpoints might be: <br /> 
<ol>
<li>getNumberOfEdits(begin, end): int <br />
<li>searchEditsForKeyword(keyword) : List[edit] <br />
<li>getNumberOfEditsWithKeyword(begin, end, keyword): int <br /><br />
</ol>
This may also have some client code that visualizes the data we get back
for example, using matplotlib <br /><br />

We will be using Python because it pairs well with flask & with
implementing REST APIs and web based applications. We are also
planning to use matplotlib for visualizing the data.

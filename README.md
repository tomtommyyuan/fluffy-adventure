# Course Search API - README

This is a simple Course Search API built using Python and Flask for Drofnats Wizarding University's course exploration platform. The API allows users to search for courses based on a textual query and returns a list of relevant courses ranked by relevance.

# Compile / Preparing to run

1.Python 3 need to be installed on your machine.

2.Install the dependencies used in the program: pip install flask

3.Go to this "search.carta" directory and launch "python search.py"

4.Go to a web browser, enter http://127.0.0.1:5000/search?keyword=

5.Type your search phrase directly after the url. e.g. http://127.0.0.1:5000/search?keyword=introduction

# Key Design Decisions

The api would be called through http experimental developer server, and "search?keyword=" must follow the root address. The design is largely self-explanatory and logical.

The search algorithm is designed to calculate a relevance score for each course based on the query input. Relevance score used for ranking.

Exact Course Code Match: if the query exactly matches the course code (case-insensitive), the course is given an infinite relevance score, ensuring it appears at the top of the results.

Keyword Matching: The query is split into keywords. Each keyword is checked against the course title and description.Matches in the title add +10 per keyword to the relevance score. Matches in the description add +5 per keyword.

To improve the user experience, the search algorithm includes additional features: accomodated query without spacing, and an additional use of string similarity index; these are designed for accomodating typos.

# Key Rationales / Tradeoffs

Flask is a lightweight web framework that is easy to set up and use for small applications. I used Flask and hardcoded data simply for simplicity, given that I'm familiar with Python and has used Flask during my Futronics (NA) Corporation internship the past summer. Using hardcoded data eliminates the need for setting up a database, allowing for quick development and testing.

The use of relevance score is a major practice in the industry, and my design decisions are made according to human logic. Handling queries without spaces and accommodating minor typos improve the search functionality, making it more forgiving and user-friendly. The specific aspects of number (e.g. using the number 10 as cutoff of determining relevance, and the specific calculations of relevant scores) are definitely debatable, and I think these decisions should be done by mathematicians and anthropologists.

# Additional Details

Super fun project!! Love to work more on it
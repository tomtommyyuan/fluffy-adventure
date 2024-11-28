from flask import Flask, request, jsonify
from difflib import SequenceMatcher

app = Flask(__name__)

# Hardcoded course data
courses = [
    {
        "id": 1,
        "title": "Intro to Magic and Mysticism",
        "description": "Introductory course for all things magic and mysticism.",
        "course_code": "MAGIC 101",
        "requirements": [
            "SpiritualInquiry"
        ],
        "units": [
            4,
            4
        ],
        "quarters": [
            "autumn",
            "winter",
            "spring"
        ]
    },
    {
        "id": 2,
        "title": "Undergraduate Independent Magical Studies",
        "description": None,
        "course_code": "MAGIC 199",
        "requirements": [],
        "units": [
            3,
            6
        ],
        "quarters": [
            "autumn",
            "winter",
            "spring",
            "summer"
        ]
    },
    {
        "id": 3,
        "title": "Intro to Potioncrafting",
        "description": "Brewing, mixing, and stirring effective magical concoctions. No prerequisites.",
        "course_code": "POTIONS 101",
        "requirements": [
            "SpiritMixingAnalysis"
        ],
        "units": [
            4,
            4
        ],
        "quarters": [
            "autumn",
            "winter",
            "spring"
        ]
    },
    {
        "id": 4,
        "title": "Advanced Potioncrafting",
        "description": "Brewing, mixing, and stirring effective and elegant magical concoctions beyond the basics. Prerequisites: POTIONS 101.",
        "course_code": "POTIONS 201",
        "requirements": [
            "SpiritMixingAnalysis"
        ],
        "units": [
            4,
            4
        ],
        "quarters": [
            "winter"
        ]
    },
    {
        "id": 5,
        "title": "AI for Spellcasting",
        "description": "Applying artificial intelligence to the ancient art of spellcasting.",
        "course_code": "MAGIC 229",
        "requirements": [],
        "units": [
            3,
            3
        ],
        "quarters": [
            "autumn",
            "spring",
            "summer"
        ]
    },
    {
        "id": 6,
        "title": "Spiritual Leadership Speaker Series",
        "description": "Leading figures in spiritual leadership discuss their professional experiences.",
        "course_code": "SPIRITS 50",
        "requirements": [
            "SpiritualInquiry"
        ],
        "units": [
            1,
            1
        ],
        "quarters": [
            "autumn",
            "winter"
        ]
    },
    {
        "id": 7,
        "title": "Potion Tasting",
        "description": "Sampling a variety of delicious and elegant potions.",
        "course_code": "POTIONS 60D",
        "requirements": [],
        "units": [
            1,
            1
        ],
        "quarters": [
            "spring"
        ]
    }
]

def search_courses(query):
    query = query.lower()
    keywords = query.split()

    results = []

    for course in courses:
        relevance_score = 0

        # Check for exact match with course code, if so, this course should have absolute priority
        if query == course['course_code'].lower():
            relevance_score += float('inf') 

        title = course['title'].lower()
        description = (course['description'] or "").lower()

        # Check for matches in the title
        title_matches = 0
        for word in keywords:
            if word in title:
                title_matches += 1
        relevance_score += title_matches * 10

        # Check for matches in the description
        desc_matches = 0
        for word in keywords:
            if word in description:
                desc_matches += 1
        relevance_score += desc_matches * 5

        # Handle queries without spaces (e.g., "introtomagic")
        title_no_space = title.replace(" ", "")
        query_no_space = query.replace(" ", "")
        if query_no_space in title_no_space:
            relevance_score += 100 

        # Calculate additional "string span" score; here, we want to do some accomodation if user has typo (e.g., "intro to msgic")
        similarity_ratio = SequenceMatcher(None, query, title).ratio()
        relevance_score += similarity_ratio * 20 
        
        # Here, we used 10 as the threshold for relevance cutoff, but it could be replaced by other number based on research
        if relevance_score > 10:
            course_copy = course.copy()
            course_copy['relevance_score'] = relevance_score
            results.append(course_copy)

    results.sort(key=lambda x: x['relevance_score'], reverse=True)

    # Remove relevance_score from the results
    for course in results:
        del course['relevance_score']

    return results


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('keyword', '').strip()

    if not query:
        return jsonify({'error': 'Query parameter "keyword" is required.'}), 400
    results = search_courses(query)

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
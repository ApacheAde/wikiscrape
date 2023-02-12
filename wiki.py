import requests
from bs4 import BeautifulSoup

def get_wikipedia_summary(term):
    # Format the Wikipedia URL
    wikipedia_url = f"https://en.wikipedia.org/wiki/{term}"

    # Make the request to the Wikipedia page
    res = requests.get(wikipedia_url)

    # Check if the request was successful
    if res.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(res.text, "html.parser")

        # Find the first two paragraphs of the page
        paragraphs = []
        for p in soup.find("div", id="mw-content-text").find_all("p"):
            paragraphs.append(p.text.strip())

        # Return the first two paragraphs
        return "\n".join(paragraphs[:2])
    else:
        return "Failed to retrieve the page content"

# Request the user's input
term = input("Enter a term, person, or thing: ")

# Get the Wikipedia summary for the input
summary = get_wikipedia_summary(term)

# Print the summary
print(summary)

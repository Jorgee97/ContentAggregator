import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/api/verge")
def pull_the_verge():
    the_verge = requests.get("http://theverge.com")
    soup = BeautifulSoup(the_verge.content, features='html.parser')

    entries = soup.find_all('a', attrs={'data-analytics-link': 'article'})
    title_link_response = list()
    for entry in entries:
        s = BeautifulSoup(str(entry), features='html.parser')
        link = s.find('a').attrs['href']
        title = s.find('a').text
        title_link_response.append({
            'link': link,
            'title': title
        })

    return jsonify(title_link_response)


if __name__ == "__main__":
    app.run()

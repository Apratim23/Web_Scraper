from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_webpage(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title=soup.title.text.strip()
        h1=soup.find('h1').text.strip() if soup.find('h1') else None
        meta_description=soup.find('meta', attrs={'name':'description'})['content'] if soup.find('meta', attrs={'name':'description'}) else None

        return jsonify({'title': title, 'h1': h1, 'meta_description': meta_description})
    else:
        print("Failed to retrieve webpage")
        return jsonify({'error': 'Failed to retrieve webpage'})

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        return scrape_webpage(url)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
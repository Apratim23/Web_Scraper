## Web_Scraper 

### Project Description
This project is a web scraping application that integrates Large Language Models (LLMs) for processing and summarizing scraped data. It utilizes Python libraries like **BeautifulSoup** and **Requests** for web scraping, and **LlamaIndex** for LLM integration. The application features a Flask backend for handling scraping tasks and queries, along with an HTML/CSS frontend for user interaction.

### Table of Contents
1. [Introduction](#introduction)
2. [Use Cases](#use-cases)
3. [Installation](#installation)
4. [Example Usage](#example-usage)
5. [Dependencies](#dependencies)
6. [How It Works](#how-it-works)
7. [Output Example](#output-example)
8. [Contributing](#contributing)
9. [License](#license)

### Introduction
This web scraper is designed to simplify the process of extracting data from websites and processing it using LLMs. It focuses on retrieving specific information by parsing HTML content, storing it in a structured format, and then using LLMs to summarize or analyze the data.

### Use Cases
- **Data Extraction**: Useful for extracting data from websites for analysis or research purposes.
- **Web Crawling**: Can be used to map and crawl through websites to gather URLs of interest.
- **Data Integration**: Integrates well with data science tools for further analysis.
- **LLM Integration**: Utilizes LLMs to process and summarize scraped data.

### Installation
To install the necessary libraries, run the following command in your terminal:
```bash
pip install beautifulsoup4 requests llama-index llama-index-readers-web scrapfly-sdk flask
```

### Example Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Web_Scraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Web_Scraper
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```

### Dependencies
- **BeautifulSoup4**: For HTML parsing.
- **Requests**: For making HTTP requests.
- **LlamaIndex**: For integrating LLMs with web scraping.
- **Scrapfly SDK**: For handling dynamic content.
- **Flask**: For creating the backend API.

### How It Works
1. **Web Crawling**: The scraper uses **Requests** and **BeautifulSoup** to navigate through websites and gather data.
2. **HTML Parsing**: **BeautifulSoup** is used to parse the HTML content of web pages.
3. **LLM Integration**: **LlamaIndex** is used to process and summarize the scraped data using LLMs.

### Output Example
The scraper outputs data in a structured JSON format. Here's a simplified example:
```json
[
  {
    "title": "Example Title",
    "description": "Example Description",
    "summary": "LLM generated summary"
  },
  {
    "title": "Another Example",
    "description": "Another Description",
    "summary": "LLM generated summary"
  }
]
```

### Contributing
Contributions are welcome! To contribute, please fork the repository and submit a pull request with your changes.

### License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

### Additional Notes
- Ensure you comply with the terms of service of the websites you scrape.
- This scraper is for educational purposes and should be used responsibly.

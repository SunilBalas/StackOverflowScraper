# Stack Overflow Scraper
This Scraper is built using Scrapy, a powerful and flexible web scraping framework for Python. It allows you to scrape information from the Stack Overflow website and save it in a structured format such as CSV or JSON.

## Installation
1. Install Scrapy using pip: 
```
pip install scrapy
```
2. Clone this repository: 
```
git clone https://github.com/SunilBalas/StackOverflowScraper.git
```
3. Navigate to the project directory: 
```
cd StackOverflowScraper
```

## Usage
To scrape all questions, description and tags for first 30 pages, run the following command:
```
scrapy crawl StackQuestionSpider -O stack_ques.json
```

To scrape all information of tags for first 5 pages, run the following command:
```
scrapy crawl StackTagSpider -O stack_tags.json
```

## Output
The scraped data will be saved in the specified output file in CSV or JSON format. The data will include the following fields:

For qeustions:
- question: The title of the question
- description: The description of the question
- tags: The tags associated with the question

For tags:
 - tag number: The serial number of the tag
 - title: The title of the tag
 - url: The url for the tag
 - desciption: The description of the tag
 - question count: Total count of questions associated with the tag

## Note
Using this scraper to scrape data from the stackoverflow website is against their terms of service. It should be used only for testing and educational purposes.
Always be respectful of the website's terms of service and robots.txt file.

## Contribution
Feel free to contribute to this project by submitting pull requests or by reporting any issues you encounter.
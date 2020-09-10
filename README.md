# NTUOSS Data scraping and Data cleaning workshop

What is web scraping and web crawling?

Most might be confused about these terms as they are used interchangably and it is important to know to when to use what given the context.

Web scraping is extracting information of any form from any source not necessarily a web page and on the other hand, web crawling is a process of iteratively finding and fetching web links starting from a list of seed URL's. Strictly speaking, to do web crawling, we have to do some degree of web scraping (to extract the URL's.)

In this workshop we see about how to crawl through various pages to scrape content from websites. Firstly, to perform there are a few libraries out there and let me give you my reasoning on why I chose the library with which we are going to work today!

So there are three standard libraries which could be used and which you might have heard about.

- Beautiful Soup
- Scrapy
- Selenium

In my opinion, scrapy is the most efficient and effective python library to scrape content from webpages. Let me give you my reasoning both Selenium and Beautifulsoup are very easy to learn and are suitable if you are trying to mine a small of amount of data from the web and on the downside, you might get blocked in some websites which require Captcha.

On the other hand, Scrapy has a much steeper learning curve but it is much more robust and very efficient compared to others. It is very much advised to use Scrapy when mining much larger data from the web.

<!-- hi siddesh u got this u so cool always flexing  -->

To sum things up, use Beuatifulsoup or Selenium if you are scraping a small amount of data and use Scrapy to scrape much larger.

Environment setup:
-> venv
-> scrapy

### Prerequisites

- Need to know how to write xpath for different sections
  - What is xpath?

## Goal of the workshop

- By the end of the workshop, we'll create two different datasets for two seperate tasks.

  1. Create an image classification dataset -> Painting vs Photographs
  2. Create an news dataset to test your sentiment analysis model

- what is noisy data?
- what does cleaning really mean? Visual Samples?

## Principles of datasets

- Ethics of modern datasets
- Address issues of gender bias

## Workshops - Hands-On-Excercises

---

- create spiders to crawl from web

- data cleaning -> images

  - create a utility script for the students

- data cleaning -> text

## References

---

- Courses
  intro
  intermed
  adnv

## Project ideas

- idea 1
- idea 2

## contact info

- email:

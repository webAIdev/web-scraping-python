# Public Web Data Scraping in 2024- Practical Blog

To evaluate the strengths and limitations of each scraping technique, we conducted a comparative analysis using three prevalent scraping methods. Our experiment dive into three distinct types of websites encountered in common scraping tasks.


## Web Scraping Techniques

### DIY Experiment: **Building Custom Scripts** with BeautifulSoup

In this experiment, we will explore custom script building for each scraping task using BeautifulSoup. This classic approach to web scraping is ideal for those who prefer a granular level of control over their data extraction process.

STEPS REQUIRED:

1. **Website Inspection**: Visit the target website. Use the browser's inspect tool to view the HTML structure, CSS, and JavaScript elements.
2. **Writing the Script**: Create a Python script using BeautifulSoup. Write code to send HTTP requests and parse the HTML content of the page.
3. **Element Identification**: Identify and select specific HTML elements (like divs, classes, or IDs) from which to scrape data.
4. **Data Scraping**: Code the script to extract text, links, or other information from the identified elements.
5. **Data Cleaning**: Clean and format the scraped data for further use or analysis.


### **The Shortcut** Experiment: **Requests Capture** with Nimble

Here, we explore the efficiency of the Requests Capture method with Nimble. This approach simplifies the process by directly capturing and utilizing network requests, ideal for users seeking a quicker path to data retrieval.

STEPS REQUIRED:

1. **Network Monitoring**: Visit the target site. Use the browser's network monitoring tool to observe API calls or network requests.
2. **Capturing Requests**: Identify the network requests that fetch the necessary data. Note the request URLs, headers, and parameters.
3. **Schema Selection and Request Creation**:
    - **Schema Decision**: Select an existing parsing schema for the target website or create a new one using Nimble Parsing Skills.
    - **Schema Evaluation**: Download and evaluate results from Parsing Skills endpoint to select the most effective schema.
    - **Recreating Requests**: Deploy the chosen schema and use Python with the **`requests`** library and Nimble’s Network Capture solution to replicate these network requests to fetch data
4. **Data Filtering**: Write Python code to extract/ filter the needed information from the responses of these requests.
5. **Data Formatting**: Use Python to convert the data into desired format for storage or analysis.


### **Web API** Experiment: Scraping with Nimble’s API

This method focuses on leveraging Nimble's Web API for scraping. It represents the cutting edge of web scraping, where ease of use meets the power of modern technology.

STEPS REQUIRED:

1. **API Configuration**: Initialize Nimble’s Web API, setting up necessary endpoints, parameters, and authentication details.
2. **Schema Selection and Request Creation**:
    - **Schema Decision**: Select an existing parsing schema for the target website or create a new one using Nimble Parsing Skills.
    - **Schema Evaluation**: Download and evaluate results from Parsing Skills endpoint to select the most effective schema.
    - **Scraping Execution**: Deploy the chosen schema with Nimble API on the target website for intelligent data extraction.
3. **Receiving Data**: Collect and process the JSON data returned by the API.
4. **Data Processing**: Use Python to convert the data from JSON to a desired format for storage or analysis.



## Experiments

1. **Simple HTML Structures** - [Powells Scraping Experiment](https://www.powells.com/featured/picks-of-the-season-2023):
    - `01-practical_blog/powells-experiment/diy-scraping/:` Demonstrates the Do-It-Yourself approach to web scraping.
    - `01-practical_blog/powells-experiment/requests-capture-approach/:` Not Applicable.
    - `01-practical_blog/powells-experiment/modern-approach/:` Explores Managed WebAPIs for efficient data extraction.

2. **JavaScript Heavy** - [BBC Scraping Experiment](https://www.bbc.com/news/world-europe-67895152):
    - `01-practical_blog/bbc-experiment/diy-scraping/:` Demonstrates the Do-It-Yourself approach to web scraping.
    - `01-practical_blog/bbc-experiment/requests-capture-approach/:` Not Applicable.
    - `01-practical_blog/bbc-experiment/modern-approach/:` Explores Managed WebAPIs for efficient data extraction.

3. **Strong Anti-Scraping Measures** - [Expedia Scraping Experiment](https://www.expedia.com/Hotel-Search?adults=&children=&destination=Dubai%2C%20Dubai%2C%20United%20Arab%20Emirates&endDate=2024-01-14&guestRating=ANY&regionId=6053839&selected=1109595&semdtl=&sort=RECOMMENDED&startDate=2024-01-12&theme=&useRewards=false&userIntent=):
    - `01-practical_blog/expedia-experiment/diy-scraping/:` Demonstrates the Do-It-Yourself approach to web scraping.
    - `01-practical_blog/expedia-experiment/requests-capture-approach/:` Focuses on the Network Requests Capture Approach using internal APIs.
    - `01-practical_blog/expedia-experiment/modern-approach/:` Explores Managed WebAPIs for efficient data extraction.



##  Results

|  |  | DIY Approach (Beautiful Soup) | Shortcut Approach (Nimble’s Network Capture) | WebAPI (Nimble’s WebAPI) |
| --- | --- | --- | --- | --- |
| 1. | Simple HTML Structures: [Powells](https://www.powells.com/featured/picks-of-the-season-2023) |  |  |  |
|  | Scrape Status | ✅ | ✅ | ✅ |
|  | Parsed Data Accuracy | ✅ Parsed Successfully  [Manual] | Parsed Successfully - Needs further cleaning &  | ✅ Parsed Successfully  |
|  | Time to Implement | ~1.5 hours | ~20 mins | Instant |
|  | Maintenance Required? | YES - For parsers, proxies, captcha solver | No Maintenance required | No Maintenance required |
|  |  |  |  |  |
| 2. | JavaScript Heavy: [BBC](https://www.bbc.com/news/world-europe-67895152) |  |  |  |
|  | Scrape Status | ⚠️ Failed | Not Applicable | ✅ |
|  | Parsed Data Accuracy | ❌ | Parsed Successfully - Needs further cleaning | Parsed Successfully - 80% accuracy |
|  | Time to Implement | ~3 hours | ~20 mins | Instant |
|  | Maintenance Required? | ⚠️ Requires advanced headless browsers, parsers, proxies, captcha solver, etc | No Maintenance required | No Maintenance required |
|  |  |  |  |  |
| 3. | Strong Anti-Scraping Measures: [Expedia](https://www.expedia.com/Hotel-Search?adults=&children=&destination=Dubai%2C%20Dubai%2C%20United%20Arab%20Emirates&endDate=2024-01-14&guestRating=ANY&regionId=6053839&selected=1109595&semdtl=&sort=RECOMMENDED&startDate=2024-01-12&theme=&useRewards=false&userIntent=) |  |  |  |
|  | Scrape Status | ⚠️ Failed | ✅ | ✅ |
|  | Parsed Data Accuracy | ❌ | ✅ Parsed Successfully  [Automated] | ✅ Parsed Successfully  [Automated] |
|  | Time to Implement | 4 hours | 10 minutes to study & filter network requests | Instant |
|  | Maintenance Required? | ⚠️ Requires integration with advanced tools for captcha solving, etc | No Maintenance required | No Maintenance required |
|  |  |  |  |  |
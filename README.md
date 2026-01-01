
# Python Web Scraper

This project is a Python 3 command-line utility designed to fetch HTML content, parse product names and prices, and save structured results to an output file. It demonstrates modular scraping, safe practices, and automated file handling, making it a clean portfolio project.

The scraper automatically creates the necessary output directories and sample HTML fixture files if they do not exist, so users don’t need to manually set anything up.

## Core Features

- **HTML Fetching:** Uses `requests` to retrieve HTML from a given URL, or reads from a local fixture file for testing purposes.
- **HTML Parsing:** Extracts product names and prices using BeautifulSoup in a structured, reliable way.
- **Automated File Management:**  
  - Creates `output/` directory automatically if missing.  
  - Saves parsed results to `output/product_details.txt`.  
- **Single Entry Point:** Run `main.py` once; it orchestrates fetching, parsing, and saving the output automatically.
- **Safe & Educational Scraping:** Designed to demonstrate parsing and scraping workflows without scraping live production websites by default.

## Technology Used & Dependencies

- **Language:** Python 3  
- **HTML Parsing:** BeautifulSoup4  
- **HTTP Requests:** Requests  
- **File I/O:** Automated directory and file creation  
- **Structure:** Modular design with separate files for fetching, parsing, and orchestration

**Files in the repository:**

- `html_fetcher.py` — Handles fetching HTML content  
- `html_parser.py` — Parses product names and prices  
- `main.py` — Single entry point  

**Directories created automatically during runtime:**

- `output/` — Stores the `product_details.txt` file   

## How to Run

### Prerequisites

1. Python 3 installed on your system.  
2. Install dependencies:
```
pip install requests beautifulsoup4
```

### Execution Steps

1. Clone the repository:
```
git clone https://github.com/szthaarnav/python-web-scraper.git
```
2. Navigate to the project directory:
```
cd python-web-scraper
```
3. Run the scraper:
```
python scraper/main.py
```
The program will automatically fetch or load HTML, parse product data, and save the results to `output/product_details.txt`.

## Notes

- Designed for educational purposes and portfolio demonstration.  
- Modular design allows easy extension to handle CSV or JSON exports in the future.  
- Uses local fixtures to prevent live scraping of production websites.  

## Example Output

Product Name:                   Price:  
Wireless Mouse                  $24.99  
Mechanical Keyboard             $79.49  
USB-C Hub                       $39.95  

Total: $144.43

## Future Improvements

- Add export options to CSV or JSON  
- Include CLI arguments for custom URLs and output file locations  
- Add unit tests for parsing logic  
- Implement logging for better debugging and tracking

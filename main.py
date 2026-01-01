from html_fetcher import fetch_html
from html_parser import parse_html,write_to_file

URL="https://web-scraping.dev/products"
HTML_OUTPUT="sample_products.html"
def main():
    fetch_html(URL,HTML_OUTPUT)
    names,prices=parse_html(HTML_OUTPUT)
    write_to_file(names,prices)

if __name__=="__main__":
    main()
import requests
# url="https://web-scraping.dev/products"
def fetch_html(url,output_html="sample_products.html"):
    r=requests.get(url)
    with open(output_html,"w") as f:
        f.write(r.text)
from bs4 import BeautifulSoup
import os

def parse_html(html_file):
    with open(html_file,"r") as f:
        html_raw=f.read()
    soup=BeautifulSoup(html_raw,'html.parser')
    html_product_names=(soup.find_all(class_="mb-0"))
    html_prices=(soup.find_all(class_="price"))
    return html_product_names,html_prices


def write_to_file(names,prices,output_text_file="Product_Details.txt"):

    #variables
    lst_product_names=["Product Name:"]
    lst_prices=["Price:"]
    lines=[]
    total=0.0

    #Looping and appending
    for j in names:
        lst_product_names.append(j.get_text(strip=True))

    for i in prices:
        each_price=i.get_text(strip=True)
        total+=float(each_price)
        lst_prices.append(each_price)

    for k in range(len(lst_product_names)):
        if k==0:
            lines.append(f"{lst_product_names[k]:<30} {lst_prices[k]:<7}")
            continue
        lines.append(f"{lst_product_names[k]:<30} {'$'+lst_prices[k]:<7}")
    total_text=f"Total: ${total:<7.2f}"
    lines.append(total_text)

    OUTPUT_DIR = "output"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, output_text_file)

    with open(output_path,"w") as p:
        p.write("\n".join(lines))

    os.startfile(output_path)
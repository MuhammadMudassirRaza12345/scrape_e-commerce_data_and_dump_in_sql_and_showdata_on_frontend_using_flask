# run1
import requests  
from bs4 import BeautifulSoup

# to save data in database
from bgallery_db import insert 
 
# first i save data in list then i insert in database 
data=[] 

# run 2

q=input("Enter your search: like hair+care ,skin+care, etc: ") 

# Run 3
url = "https://bagallery.com/search?type=product&filter=1&q={q}"
 

payload={}
headers = {
  'Cookie': '_landing_page=%2Fsearch%3Ftype%3Dproduct%26filter%3D1%26q%3Dskin%2Bcare; _orig_referrer=; _s=e24e6294-5097-49cf-af4f-71d2383cd361; _shopify_s=e24e6294-5097-49cf-af4f-71d2383cd361; _shopify_y=0d78bc90-7e5f-4df7-8db1-d60434f30b0a; _y=0d78bc90-7e5f-4df7-8db1-d60434f30b0a; localization=PK; secure_customer_sig='
}

# run 4
response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

# run 5 
soup = BeautifulSoup(response.content, "html.parser")

div_of_product_title=soup.select('div.grid-item')

for i in div_of_product_title:
    product_name=i.select_one('div.grid-item div.product-bottom a.product-title span').text.strip()  
    try:
        product_price=i.select_one('div.grid-item div.product-bottom span.old-price.span.money').text.strip() 
        product_special_price=i.select_one('div.grid-item div.product-bottom span.special-price.span.money').text.strip()
    except:
        product_price=i.select_one('div.grid-item div.product-bottom span.money').text.strip() 
        discount_price="No Special Price discount"
    product_image=i.select_one('div.grid-item div.product-item div.product-image a')['href'] 
    # print(product_name,product_price,discount_price,product_image,"\n","\n")
    dict_data1=(product_name,product_price,discount_price,product_image)   
    data.append(dict_data1)  
    
# to insert data in database 
insert(data)

# and you can view data in database through running app_flask.py file

 









# print(soup.prettify())

# div_of_product_title=soup.select('div.grid-item')
# print(div_of_product_title)


# div_of_product_inner_title=soup.select('div.grid-item div.product-item') 
# print(div_of_product_inner_title)



# product_name=soup.select_one('div.grid-item div.product-bottom a.product-title span') 

# product_price=soup.select_one('div.grid-item div.product-bottom span.money').text.strip()
# print(product_price)

# product_special_price=soup.select_one('div.grid-item div.product-bottom span.money').text.strip()
# print(product_special_price)

 

# div_image=soup.select('div.grid-item div.product-item div.product-image a') 
# print(div_image)
 
# actual_web_links = [web_link['href'] for web_link in div_image]  
# print(actual_web_links[0])


# project_href = [i['href'] for i in  div_image.find_all('a', href=True)]
# print(project_href)


 
    


# print(data)    
    # dict_data=(
    #     product_name,
    #     product_price,
    #     product_special_price,
    #     product_image
    # )
    # data.append(dict_data)
# insert(data) 
# print(data)   
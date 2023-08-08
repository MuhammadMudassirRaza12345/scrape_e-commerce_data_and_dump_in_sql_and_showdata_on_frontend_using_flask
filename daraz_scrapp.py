
#------------------------------------- Data scraping from Daraz.pk----------------------------------------------------------------
import requests , json
from daraz_db import insert 

# run this file to like pyhton app_scrapp.py

# here we are going to scrape data from daraz.pk and store it in our database
data=[] 



user_search=input("Enter your search: ")
pages=int(input("Enter number of pages: "))
for i in range(1,pages+1):
    url = "https://www.daraz.pk/catalog/"
    payload={}
    Query_String_Parameters = {
        "_keyori": "ss",
        "ajax": "true",
        "from": "input",
        "page": i,
        "q":  user_search, 
        "spm": "a2a0e.searchlist.search.go.6d331e20o8s8EK"
        }
    headers = {
        'authority': 'www.daraz.pk',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ru;q=0.7',
        'content-type': 'application/json',
        'cookie': '_uab_collina=167544282773236949058858; _schn=_tddd8a; lzd_cid=8aab558c-4db2-4142-8308-534ee1d97dc8; t_uid=8aab558c-4db2-4142-8308-534ee1d97dc8; lzd_sid=19b882c7997ca510269ecca3d00d0d21; _tb_token_=7e1e65b0e3e7b; hng=PK|en-PK|PKR|586; userLanguageML=en-PK; t_fv=1675442829208; cna=jChkHFKGvT0CAW4m9cH8m6MG; _gcl_au=1.1.1002079961.1675442830; _gid=GA1.2.1840968353.1675442830; __auc=b9067007186182cbbcff27658e8; _scid=752eb98f-2b3c-443d-bbde-e3ebf77e6f9b; _fbp=fb.1.1675442831300.1515930116; _bl_uid=m9lsgdz7o5Cr8geU2ka6aC6k1L6b; _sctr=1|1675364400000; mi_p_source=undefined; mi_p_medium=undefined; mi_p_campaign=undefined; mi_p_term=undefined; mi_p_content=undefined; mi_p_gclid=undefined; xlly_s=1; XSRF-TOKEN=fea416b5-65ab-42aa-9e13-f00b6c6e3195; _gcl_marco=1.1656473956.1675443370; t_sid=LiGqlaRFonc7feZWo2JWpFeeR8JB4Ogs; utm_channel=NA; daraz-marketing-tracker=hide; __asc=729784e41861aae5046429c3176; _m_h5_tk=c046926fa917c97ab9f2e0b79b7f9d0e_1675495316089; _m_h5_tk_enc=68324bd0eafb6bb8d53d3f54261cbab9; JSESSIONID=9B72F70CD6D17333E8EA03AE96638EB0; _ga=GA1.2.1084556584.1675442830; _ga_5L4FRV3KPW=GS1.1.1675484876.4.1.1675485141.60.0.0; tfstk=cgelBbZWI7lSfUBLlzM5IbnVzcfAa2-rPfh43iMCsRsSHIeo4sV6gCShjUgV5aRC.; l=fBPp8qzrTVHbDeZvBO5alurza779yIRf1sPzaNbMiIEGa6ChtFasgNCedjyJSdtjQT5qietz_ANlDd3HS5UU-xsUt8mUjhP22Qv6JeZ-cS1V.; isg=BLu7SkM1XB9mjWCrpzrlee6zSp8lEM8S_nenSa14I7rEDNjuNeMfY3cKJrRCLCcK; JSESSIONID=4F5CB4E2B7C10A47D0DA4A5BA2DB1B6D',
        'referer': 'https://www.daraz.pk/catalog/?_keyori=ss&from=input&page=1&q=haircare&spm=a2a0e.searchlist.search.go.6d331e20o8s8EK',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, params=Query_String_Parameters).json()
    row=response['mods']['listItems']
    
    for i in range(0,len(row)):
        product_id=response['mods']['listItems'][i]['nid']
        name=response['mods']['listItems'][i]['name']
        product_image_url=response['mods']['listItems'][i]['image']
        product_current_price=response['mods']['listItems'][i]['price']
        productUrl=response['mods']['listItems'][i]['productUrl']
        try :
            product_original_price=response['mods']['listItems'][i]['originalPrice']
            discount=response['mods']['listItems'][i]['discount']
        except:
            product_original_price= product_current_price
            discount='No Discount'
        dict_data=(
            product_id,
            name,
            product_image_url,
            product_original_price,
            discount,
            product_current_price,
            productUrl)
        data.append(dict_data)
      

# this is the code for insert data in database 
insert(data)
# -----------------------------To view the search  data ----------------------------
# go to the app_flask(db).py and run the code by :python app_flask(db).py










# from flask import Flask ,jsonify 

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return jsonify(data)


# if __name__ == '__main__':
#     app.run(debug=True, port=8000)


#  python -m pip install "connexion[swagger-ui]==2.14.1"

























# @app.get("/")
# async def root():
#     return data
        
# df=pd.DataFrame(data)
# df



# row=response['mods']['listItems']
# print(response['mods']['listItems'][1])
# product_id=response['mods']['listItems'][1]['nid']
# print(product_id)
# name=response['mods']['listItems'][1]['name']
# print(name)
# product_image=response['mods']['listItems'][1]['image']
# print(product_image)
# product_original_price=response['mods']['listItems'][1]['price']
# print(product_original_price)
# print(len(response['mods']['listItems']))





# print(data)


# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile, indent=4)
    # print(product_id)
    # print(name)
    # print(product_image_url)
    # print(product_original_price)
    # print(discount)
    # print(product_current_price)
    # print(productUrl)
    # print('.........................................')
    



# 

#To view data using api
# 


# @app.get("/")
# async def root():
#     return data  

# for run code :uvicorn app3:app --reload
 
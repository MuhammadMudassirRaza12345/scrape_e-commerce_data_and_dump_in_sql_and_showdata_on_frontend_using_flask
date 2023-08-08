# scrape_e-commerce_data_and_dump_in_sql_and_showdata_on_frontend_using_flask

### case:
     You are given a task to scrape data from an Ecommerce store on a daily basis for market research. You have 
     to scrape data from more than 1 website      that lists similar products (eg. Daraz and Bagallary). This 
     scraper will be running at 8:00 AM daily. Also for the testing of Non IT people you have to add an rest
     API layer so that anyone can see the results using api endpoint. You have to submit at least 2 days of 
     data in a sql file along with code.
### Instructions:
         Write a python script (.py) not a jupyter notebook.
         
### Task 1: Write a web scraper to scrape keywords results from following websites.
 Website1 :  https://www.daraz.pk/ 
 
 Website2 :  https://bagallery.com/ 

 ### Instructions:
          1)Scrape both Ecommerce sites with multiple pages or maximum 100 results for each keyword.
          
          2)Keywords for each sites are “hair care”, “skin care” and “hair fall solution” Your rest
          api should be able to do these two task:
                  a)Run the code at 8:00 AM and also save the results in DB or google sheet.
                  
                  b)Run the scraper code for the user when he visits the endpoint. E.g you 
                  have an api endpoint like localhost/scraper/api/v1/<daraz or bagallary>/<search keyword>/
                  when a user hits this url it should show the relevant results in Json format.

![Example](https://github.com/MuhammadMudassirRaza12345/scrape_e-commerce_data_and_dump_in_sql_and_showdata_on_frontend_using_flask/blob/main/Screenshot%20from%202023-08-08%2014-24-00.png)              

           
      A) Write scraper to scrape data from Ecommerce sites according to above requirements.
      
      B) Create a source location (remote database, local database or google sheet) to store 
      daily data using python library/code, first priority is to create a remote database or 
      google sheet and upload data into that if not then upload data into the local mysql table.

###  Solution
      For Daraz:
        . daraz_scrapp.py
        . daraz_db.py
        . daraz_flask.py

      For bgallery:
        . bgallery_scrapp.py
        . bgallery_db.py
        . bgallery_flask.py  
        
      [Run scrapp file in this way]()
        
           
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)      

### Task 2: Write queries using the ORG database we have used in class.       
    1)Write an SQL query to show the second highest salary from a table.
    
    2)Write an SQL query to determine the 5th highest salary without using the limit method.

    3)Write an SQL query to clone a new table from another table.

    4)Write an SQL query to show only odd rows from a table.

### Task 3: change cron job into human command and human to cron jobs.
     1) 0 17 * * 0-5
     2) 11 5 * * 5,6 
     3) every Monday midnight 
     4) 0 */6 * * * 
     5) 0 7,17 * * * 
     6) * * * * *  sleep 15; /scripts/script.sh 

      

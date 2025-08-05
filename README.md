# cidre-allen
## pandas cleaning
import pandas as pd
df=pd.read_csv('data.csv') -took the dataset
fill_avg=df.fillna(df.mean()) -filled missing data with mean of the column
sum_avg=fill_avg.mean() -gives summary of average marks 
print("Cleaned data:") - printing the values
print(fill_avg)
print("Average of the cleaned data:")
print(sum_avg)

##exception
def process_excel(file_path,col):
    error_data=[] - initialized 2 lists
    data=[]
    for i in os.listdir(file_path): -checks each file in directory using os
        if i.endswith('.xlsx'): -finds excell extention files
            try:
                df = pd.read_excel(file_path) -reads data
                df_data = df[col]
                data.append(df_data)
            except Exception as e:
                error_data.append(f"Error in {i}: {e}") -appends error data into the list
    return error_data -returns the error list

---
##time-complexitiy
arr = [i for i in range(100000)] -takes list of 1 million numbers
target=2 - set a target
s=set() - set function is used as it doesnt keep duplicates
for i in arr: -checks from 0 to 1 million
    if target - i in s: 
        print("Pair found:", i, target - i)
        break
    s.add(i) -if not found, added to set
---
##oops
class Book: -made class for books
    def __init__(self, title,author,availablility_status):
        self.title = title
        self.author = author
        self.availablility_status = availablility_status
    def borrow(self): -gave two functions for returning and borrowing
        if self.availablility_status:
            self.availablility_status = False
            print("You borrowed '{self.title}' by '{self.author}'")
        else:
            print("'{self.title}' is currently not available.")
    def return_b(self):
        self.availablility_status = True
        print("You returned '{self.title}' by '{self.author}'")

class Library: -made a class for library
    def __init__(self): 
        self.books = []
    def add(self, book):
        self.books.append(book)
    def find_b(self, title):
        for i in self.books:
            if i.title == title:
                return i
        return None
    

title=input("Enter the book title: ")
author=input("Enter the book author: ")
obj= Book(title, author, True) -took the input and set availability as true and made an object
lib= Library() -made object for library
lib.add(obj)
title= input("Enter the book title to borrow: ") -code to borrow or return
book = lib.find_b(title) 
if book:
    book.borrow()
else:
    print("Book not found in the library.")
title= input("Enter the book title to return: ")
book = lib.find_b(title)
if book:
    book.return_b()

##api
import pandas as pd -imported neccesery packages
import requests
import time

api_url = "url" -taking the url for api
weather_info = [] -creates an empty list
while True: -inside loop
    response = requests.get(api_url) -takes response from utl
    w_d = response.json() -convert this to python dictionary
    dic = {'temp': w_d[temp],'humidity': w_d[humidity]} -taking neccesery values ie tempreature and humidity
    data= pd.DataFrame(dic) -made it as a dataframe 
    weather_info.append([data]) -append to an variable
    weather_info=weather_info.to_csv("weather_info.csv") -converts and store it in csv
    time.sleep(3600) -takes value after 1 hour

--
##parsing
with open('C:/Users/hp/Downloads/sample_logs.txt') as file: -opens file
    for i in file: -checks all file
        if 'ERROR' in i: -if 'error' in line prints the line
            print(i)

    







    




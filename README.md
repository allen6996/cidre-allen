# cidre-allen

## Pandas Cleaning

```python
import pandas as pd

df = pd.read_csv('data.csv')  # Took the dataset
fill_avg = df.fillna(df.mean())  # Filled missing data with mean of the column
sum_avg = fill_avg.mean()  # Gives summary of average marks

print("Cleaned data:")
print(fill_avg)
print("Average of the cleaned data:")
print(sum_avg)
```

## Exception Handling in Excel Processing

```python
import pandas as pd
import os

def process_excel(file_path, col):
    error_data = []  # Initialized list for errors
    data = []  # List to store valid data
    
    for i in os.listdir(file_path):  # Checks each file in directory using os
        if i.endswith('.xlsx'):  # Finds Excel files
            try:
                df = pd.read_excel(os.path.join(file_path, i))  # Reads data
                df_data = df[col]  # Extracts specific column
                data.append(df_data)
            except Exception as e:
                error_data.append(f"Error in {i}: {e}")  # Appends error info
    return error_data  # Returns the error list
```

## Time Complexity for Pair Sum

```python
arr = [i for i in range(1000000)]  # List of 1 million numbers
target = 2  # Target value
s = set()  # Set to store seen numbers

for i in arr:
    if target - i in s:
        print("Pair found:", i, target - i)
        break
    s.add(i)
```

## OOPs - Library System

```python
class Book:
    def __init__(self, title, author, availablility_status):
        self.title = title
        self.author = author
        self.availablility_status = availablility_status

    def borrow(self):
        if self.availablility_status:
            self.availablility_status = False
            print(f"You borrowed '{self.title}' by '{self.author}'")
        else:
            print(f"'{self.title}' is currently not available.")

    def return_b(self):
        self.availablility_status = True
        print(f"You returned '{self.title}' by '{self.author}'")

class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def find_b(self, title):
        for i in self.books:
            if i.title == title:
                return i
        return None

title = input("Enter the book title: ")
author = input("Enter the book author: ")
obj = Book(title, author, True)  # Create Book object
lib = Library()  # Create Library object
lib.add(obj)

title = input("Enter the book title to borrow: ")
book = lib.find_b(title)
if book:
    book.borrow()
else:
    print("Book not found in the library.")

title = input("Enter the book title to return: ")
book = lib.find_b(title)
if book:
    book.return_b()
```

## API - Weather Info to CSV

```python
import pandas as pd
import requests
import time

api_url = "url"  # API endpoint
weather_info = []  # Empty list to collect data

while True:
    response = requests.get(api_url)  # Takes response from URL
    w_d = response.json()  # Converts JSON to Python dict
    
    dic = {'temp': w_d['temp'], 'humidity': w_d['humidity']}  # Extracts needed values
    data = pd.DataFrame([dic])  # Create DataFrame from dict
    
    weather_info.append(dic)  # Append dictionary to list
    
    pd.DataFrame(weather_info).to_csv("weather_info.csv", index=False)  # Save to CSV
    time.sleep(3600)  # Sleep for 1 hour
```

## Parsing Log Files

```python
with open('C:/Users/hp/Downloads/sample_logs.txt') as file:  # Opens file
    for i in file:  # Checks each line
        if 'ERROR' in i:  # If 'ERROR' in line, print the line
            print(i)
```

# OC Projet 2 : Utilisez les bases de Python pour l'analyse de marché

# Introduction 
Created multiple scripts in python to extract information from a bookstore website https://books.toscrape.com/ I created 3 files which i will explain in the following : 

The first file is OneBook.py it's extract information for a book i chose (you can change the book by modifing the url)
then it writes the information into a CSV file with the title of the book as its file name

The second file is OneCategory.py it's extract information for a category i chose (you can change the category by modifing the url)
it extracts the books from that category including additional pages then it writes it into a CSV file

The last file is Main.py its extracts informations of each book by category each then it writes a CSV file for each category books
it also download the cover from each book and put them into a folder called "images" 

# Installation 

First make sure you have Python installed into your system 
``` Download python here : https://www.python.org/downloads/ ```

Then you need to set up your virtual environment : 
```python3 -m venv env```

After that you need to download the requirements
```pip install -r requirements.txt```

You are now ready to use the scripts choose the appropreciate script based on what you need to execute it write this 
```python3 "name of the file".py```



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title(self):
        return "Title: " + self.title
    def get_author(self):
        return "Author: " + self.author
PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")
print(PP.title)        
print(PP.author)        
print(PP.get_title())   
print(PP.get_author())  
print(H.title)         
print(H.author)         
print(H.get_title())    
print(H.get_author())   
print(WP.title)   
print(WP.author)    
print(WP.get_title())   
print(WP.get_author())  
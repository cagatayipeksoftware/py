import pyshorteners
url=input("Enter your URL")
s= pyshorteners.Shortener()
print("the sort",s.tinyurl.short(url))
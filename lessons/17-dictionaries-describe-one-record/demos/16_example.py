book = {
    "title": "Python Notes",
    "author": "Jay",
    "pages": 200,
}
book["read"] = False
book["pages"] = 210
print(f"{book['title']} by {book['author']}, {book['pages']} pages")
print(book.get("note", "No note"))

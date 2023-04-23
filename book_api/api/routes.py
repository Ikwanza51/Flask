from api import app,Book,db
from flask import jsonify,request

@app.route('/')
def home():
    return "Home Page"

@app.route('/books')
def get_all_books():
    books = Book.query.all()
    return jsonify([book.to_json() for book in books])

@app.route('/book/<int:id>')
def get_book(id):
    book = Book.query.get(id)
    return book.to_json()

@app.route('/book/update/<int:id>',methods=['POST'])
def update_book(id):
    data = request.json
    book = Book.query.get(id)
    if book:
        if 'author' in data:
            book.author = data['author']
        if 'price' in data:
            book.price = data['price']
        if 'title' in data:
            book.title = data['title']
        db.session.add(book)
        db.session.commit()
    else :
        return "Book Not Found"
    return "Book updated"

@app.route('/book/delete/<int:id>',methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    else:
        return "Book Not Found"
    return "Deleted book"

@app.route('/book/create',methods=['POST'])
def create_book():
    data = request.json
    book = Book.query.get(data['id'])
    if book and data['id'] == book.id:
            return "Book Already Created"
    else:
        book1 = Book(author = data['author'],price = data['price'],title = data['title'],id = data['id'])
        db.session.add(book1)
        db.session.commit()
    
    return "Created BOOK"
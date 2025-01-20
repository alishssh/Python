from myapp.models import Author, Book
#create
author = Author.objects.create(name="J.K. Rowling", email="jkrowling@gmail.com")
book = Book.objects.create(title="Harry Potter", publication_date="2001-07-21", author=author)
#read
authors = Author.objects.all()

author = Author.objects.get(id=1)

books = author.books.all()
#update
author.name = "Joanne rowling"
author.save()
#delete
author =Author.objects.get(id=1)
author.delete()



from repository import Repository

from library import Library

from search import Search

from printer import show

repo = Repository()

library = Library(

    repo.load()

)

results = Search().by_language(

    library.all(),

    "Python"

)

show(results)

# TODO Найдите количество книг, которое можно разместить на дискете

size = 1.44
pages_in_book = 100
lines_in_page = 50
symbols_in_line = 25
storage_for_symbol = 4

size_kb = size * 1024
book = (((symbols_in_line * lines_in_page) * pages_in_book) * 4) / 1024

fit_books = int(size_kb // book) #приводим к int
print("Количество книг, помещающихся на дискету:", fit_books)

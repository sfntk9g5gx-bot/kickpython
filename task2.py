# TODO Найдите количество книг, которое можно разместить на дискете
disk_capacity_mb = 1.44
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024

pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
chars_total = pages * lines_per_page * chars_per_line
book_size_bytes = chars_total * bytes_per_char
books_fit = int(disk_capacity_bytes // book_size_bytes)
print("Количество книг, помещающихся на дискету:", books_fit)


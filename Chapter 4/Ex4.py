class Book:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def display_info(self):
        print("Mã sách:", self.book_id)
        print("Tên sách:", self.title)
        print("Tác giả:", self.author)
        print("Trạng thái:", self.status)
        print()


class LibraryManager:
    def __init__(self):
        self.book_list = []

    def add_book(self, new_book):
        self.book_list.append(new_book)
        print("Thêm sách thành công")

    def display_all(self):
        if len(self.book_list) == 0:
            print("Thư viện chưa có sách")
        else:
            for book in self.book_list:
                book.display_info()

    def borrow_book(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                if book.status == "Available":
                    book.status = "Borrowed"
                    print("Mượn sách thành công")
                else:
                    print("Sách này đã được mượn")
                return

        print("Không tìm thấy sách")


def main():
    manager = LibraryManager()

    while True:
        print("===== QUẢN LÝ THƯ VIỆN =====")
        print("1. Thêm sách mới")
        print("2. Hiển thị tất cả sách")
        print("3. Mượn sách")
        print("4. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            book_id = input("Nhập mã sách: ")
            title = input("Nhập tên sách: ")
            author = input("Nhập tác giả: ")

            new_book = Book(book_id, title, author)
            manager.add_book(new_book)

        elif choice == "2":
            manager.display_all()

        elif choice == "3":
            book_id = input("Nhập mã sách muốn mượn: ")
            manager.borrow_book(book_id)

        elif choice == "4":
            print("Thoát chương trình")
            break

        else:
            print("Lựa chọn không hợp lệ")

        print()


main()
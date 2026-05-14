class Pet:
    def __init__(self, pet_id, name, species, price):
        self.__pet_id = pet_id
        self.name = name
        self.species = species
        self.price = price

    def get_pet_id(self):
        return self.__pet_id

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_price(self):
        return self.price

    def display_info(self):
        print("Mã thú cưng:", self.__pet_id)
        print("Tên:", self.name)
        print("Loài:", self.species)
        print("Giá:", self.price)
        print()


class StoreService:
    def __init__(self):
        self.inventory = []
        self.revenue = 0.0

    def add_pet(self, pet):
        self.inventory.append(pet)
        print("Thêm thú cưng thành công")

    def view_inventory(self):
        if len(self.inventory) == 0:
            print("Cửa hàng chưa có thú cưng")
        else:
            for pet in self.inventory:
                pet.display_info()

    def sell_pet(self, pet_id):
        for pet in self.inventory:
            if pet.get_pet_id() == pet_id:
                self.inventory.remove(pet)
                self.revenue += pet.get_price()
                print("Bán thú cưng thành công")
                return

        print("Không tìm thấy thú cưng")

    def view_total_revenue(self):
        print("Tổng doanh thu:", self.revenue)


class ConsoleView:
    def __init__(self):
        self.store_service = StoreService()

    def run(self):
        while True:
            print("===== QUẢN LÝ CỬA HÀNG THÚ CƯNG =====")
            print("1. Thêm thú cưng mới")
            print("2. Xem danh sách thú cưng")
            print("3. Bán thú cưng")
            print("4. Xem tổng doanh thu")
            print("5. Thoát")

            choice = input("Nhập lựa chọn của bạn: ")

            if choice == "1":
                pet_id = input("Nhập mã thú cưng: ")
                name = input("Nhập tên thú cưng: ")
                species = input("Nhập loài thú cưng: ")
                price = float(input("Nhập giá: "))

                pet = Pet(pet_id, name, species, price)
                self.store_service.add_pet(pet)

            elif choice == "2":
                self.store_service.view_inventory()

            elif choice == "3":
                pet_id = input("Nhập mã thú cưng muốn bán: ")
                self.store_service.sell_pet(pet_id)

            elif choice == "4":
                self.store_service.view_total_revenue()

            elif choice == "5":
                print("Thoát chương trình")
                break

            else:
                print("Lựa chọn không hợp lệ")

            print()


app = ConsoleView()
app.run()
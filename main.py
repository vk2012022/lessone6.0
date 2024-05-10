class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users = []

    def add_user(self, user):
        # Проверка существования пользователя с таким же ID
        user_exists = False
        for u in self.__users:
            if u.get_user_id() == user.get_user_id():
                user_exists = True
                break

        if not user_exists:
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Пользователь с таким идентификатором уже существует.")

    def remove_user(self, user_id):
        found = False
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"Пользователь {user.get_name()} с идентификатором - {user.get_user_id()} удален из списка.")
                found = True
                break  # Выход из цикла после удаления пользователя
        if not found:
            print("Пользователя с таким идентификатором не существует.")


    def list_users(self):
        for user in self.__users:
            print(f"Идентификатор: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Создаем администратора
admin = Admin("001", "Алексей")

# Создаем пользователей
user1 = User("002", "Василий")
user2 = User("003", "Светлана")

# Добавляем пользователей через администратора
admin.add_user(user1)
admin.add_user(user2)

# Выводим список всех пользователей
print("Список всех пользователей:")
admin.list_users()

# Удаляем пользователя
admin.remove_user("002")

# Выводим список
print("Список всех пользователей:")
admin.list_users()


#Проверка того,что атрибуты классов защищены от прямого доступа и модификации снаружи.

user = User("005", "Михаил")
admin1 = Admin("006", "Николай")

# Попытка доступа к приватным атрибутам !!!
try:
    print(user.__name)
except AttributeError as e:
    print(f"Доступ запрещен: {e}")

try:
    print(admin1.__access_level)
except AttributeError as e:
    print(f"Доступ запрещен: {e}")


# Проверка исходного значения имени
print(user.get_name())  # Выведет "Михаил"
print(admin1.get_name())  # Выведет "Михаил"

# Попытка изменить приватный атрибут, на самом деле создает новый атрибут
user.__name = "Эдуард"
print(user.__name)  # Выведет "Эдуард"
admin1.__name = "Эдуард"
print(admin1.__name)  # Выведет "Эдуард"

# Проверка значения приватного атрибута через метод
print(user.get_name())  # Все еще выводит "Михаил", так как исходный атрибут не изменился
print(admin1.get_name())  # Все еще выводит "Николай", так как исходный атрибут не изменился
user.set_name("Григорий")
print(user.get_name())  # Выведет "Григорий"



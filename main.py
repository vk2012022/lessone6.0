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
        if not any(u.get_user_id() == user.get_user_id() for u in self.__users):
            self.__users.append(user)
            print(f"Работник {user.get_name()} добавлен.")
        else:
            print("Работник с таким идентификатором уже существует.")

    def remove_user(self, user_id):
        user = next((u for u in self.__users if u.get_user_id() == user_id), None)
        if user:
            self.__users.remove(user)
            print(f"Работник {user.get_name()} удален из списка.")
        else:
            print("Работника с таким идентификатором не существует.")

    def list_users(self):
        for user in self.__users:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

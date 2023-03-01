class User:
    """User registration/authentication"""

    def __init__(
        self,
        login: str,
        password: str,
        email: str,
        name: str,
        surname: str,
        age: str
    ) -> None:
        self.login = login
        self.password = password
        self.email = email
        self.name = name
        self.surname = surname
        self.age = age
        self.admin = False
    
    @staticmethod
    def administration(
        user: "User"
    ) -> str:
        user.admin = True
        return True



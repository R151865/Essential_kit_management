

from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.models import User

from essentials_kit_management.exceptions.exceptions import (
    InvalidPassword, InvalidUsername
)

class UserStorageImplementation(UserStorageInterface):

    def create_user(self,
                    name: str,
                    phone_number: int,
                    password: str):
        pass

    def validate_password(self, password: str):

        is_valid_password = User.objects.filter(password=password).exists()
        in_valid_password_given = not is_valid_password

        if in_valid_password_given:
            raise InvalidPassword

    def validate_username(self, username: int, password: str):

        user_obj = User.objects.filter(username=username,
                                       password=password)
        invalid_username_given = not user_obj.exists()

        if invalid_username_given:
            raise InvalidUsername

        user_id = user_obj.first().id
        return user_id
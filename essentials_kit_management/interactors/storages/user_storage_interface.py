from abc import ABC, abstractmethod

from essentials_kit_management.interactors.storages.dtos import (
    UserDto)

class UserStorageInterface():

    def create_user(self,
                    name: str,
                    phone_number: int,
                    password: str):
        pass

    def validate_password(self, password: str):
        pass

    def validate_username(self, username: int, password: str):
        pass

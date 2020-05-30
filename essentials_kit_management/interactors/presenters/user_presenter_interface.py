from abc import ABC, abstractmethod


class UserPresenterInterface():

    def raise_invalid_password_exception(self, password: str):
        pass

    def raise_invalid_username_exception(self, username: int):
        pass

    def get_access_token_response(self, acces_token_dto): # need to write acces token dto
        pass
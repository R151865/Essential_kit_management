from abc import ABC, abstractmethod


class FormPresenterInterface():

    def get_forms_response(self, form_dtos):
        pass

    def raise_invalid_form_id_exception(self):
        pass

    def get_form_to_fill_response(self, form_dto):
        pass

    def get_form_response(self, get_form_details_dto):
        pass
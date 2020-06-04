import json

from django.http import HttpResponse
from common.oauth2_storage import OAuth2SQLStorage

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation
from essentials_kit_management.presenters.user_presenter_implementation import \
    UserPresenterImplementation
from essentials_kit_management.interactors.user_login_interactor import \
    UserLoginInteractor

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_data = kwargs["request_data"]
    username = request_data["username"]
    password = request_data["password"]

    user_storage = UserStorageImplementation()
    user_presenter =  UserPresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()
    interactor = UserLoginInteractor(user_storage=user_storage,
                                     user_presenter=user_presenter,
                                     oauth2_storage=oauth2_storage)

    access_token_dict = interactor.user_login(username=username,
                                              password=password)

    access_token_dict_json = json.dumps(access_token_dict)

    response = HttpResponse(access_token_dict_json, status=200)
    return response

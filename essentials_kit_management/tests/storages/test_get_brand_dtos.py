import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import  (
    BrandDto, ItemDto)


@pytest.mark.django_db
def test_get_brand_dtos_wit_valid_details_return_dtos(create_users,
                                                      create_brands,
                                                      create_items,
                                                      create_orders,
                                                      create_sections,
                                                      create_forms):

    # Arrange
    item_dtos = [
        ItemDto(item_id=1,
                name="item1",
                description="item1",
                brand_id=1),
        ItemDto(item_id=2,
                name="item2",
                description="item2",
                brand_id=2)
    ]

    expected_brand_dtos = [
        BrandDto(brand_id=1,
                 name="brand1",
                 min_quantity=1,
                 max_quantity=5,
                 price_per_item=100),
        BrandDto(brand_id=2,
                 name="brand2",
                 min_quantity=2,
                 max_quantity=8,
                 price_per_item=200)
    ]

    storage = FormStorageImplementation()

    # Act
    actual_brand_dtos = storage.get_brand_dtos(item_dtos)

    # Assert
    assert actual_brand_dtos == expected_brand_dtos

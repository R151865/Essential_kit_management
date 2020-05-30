import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    OrderDto, ItemDto
    )


@pytest.mark.django_db
def test_get_item_dtos_with_valid_details_return_dtos(create_users,
                                                      create_brands,
                                                      create_items,
                                                      create_orders,
                                                      create_sections,
                                                      create_forms):

    # Arrange
    order_dtos = [
        OrderDto(
            order_id=1,
            user_id=1,
            item_id=1,
            brand_id=1,
            form_id=1,
            section_id= 1,
            count=10,
            pending_count=5,
            out_of_stock=0)
        ]
    expected_items_dtos = [
        ItemDto(item_id=1,
                name="item1",
                description="item1",
                brand_id=1)
        ]
    
    storage = FormStorageImplementation()

    # Act
    actual_items_dtos = storage.get_item_dtos(order_dtos)

    # Assert
    assert actual_items_dtos == expected_items_dtos

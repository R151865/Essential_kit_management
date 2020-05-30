import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import SectionDto


@pytest.mark.django_db
def test_get_form_section_dtos_with_valid_details_return_dtos(create_users,
                                                              create_brands,
                                                              create_items,
                                                              create_orders,
                                                              create_sections,
                                                              create_forms):

    # Arrange
    form_id = 1

    expected_section_dtos = [
        SectionDto(
            section_id=1,
            name="section1",
            description="section1")
        ]

    storage = FormStorageImplementation()

    # Act
    actual_section_dtos = storage.get_form_sections_dtos(form_id=form_id)

    # Assert
    assert expected_section_dtos == actual_section_dtos

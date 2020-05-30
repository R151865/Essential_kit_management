import datetime

import pytest

from essentials_kit_management.interactors.storages.dtos import (
    HomePageFormDto, GetFormBrandDto, GetFormDto, GetFormSectionDto,
    BrandDto, GetFormItemOrderDto, GetFormItemDto
    )



@pytest.fixture()
def get_forms_response_list():
    home_page_form_dtos = [
        HomePageFormDto(form_id=1,
                        name="FORM1",
                        status="LIVE",
                        close_date=datetime.datetime(2020,10,10,0,0),
                        expected_delivery_date=datetime.datetime(
                            2020,10,10,0,0),
                        items_count=20,
                        estimated_cost=3000,
                        items_pending_count=5,
                        cost_incurred_for_delivery=2000),
        HomePageFormDto(form_id=2,
                        name="FORM2",
                        status="CLOSED",
                        close_date=datetime.datetime(2020,10,10,0,0),
                        expected_delivery_date=datetime.datetime(
                            2020,10,10,0,0),
                        items_count=5,
                        estimated_cost=1000,
                        items_pending_count=5,
                        cost_incurred_for_delivery=0)
        ]
    return home_page_form_dtos

@pytest.fixture()
def get_forms_expected_dict():
    dict_form = { 
        "forms": [
                    {
                        "form_id": 1,
                        "form_name": "FORM1",
                        "form_status": "LIVE",
                        "close_date": "10th October 12AM",
                        "expected_delivery_date": "10th October 12AM",
                        "items_count": 20,
                        "estimated_cost": 3000,
                        "items_pending_count": 5,
                        "cost_incurred": 2000,
                    },
                    {
                        "form_id": 2,
                        "form_name": "FORM2",
                        "form_status": "CLOSED",
                        "close_date": "10th October 12AM",
                        "expected_delivery_date": "10th October 12AM",
                        "items_count": 5,
                        "estimated_cost": 1000,
                        "items_pending_count": 5,
                        "cost_incurred":0,
                    }
                ],
        "total_forms_count": 2
        }
    return dict_form
        





@pytest.fixture()
def get_form_details_dto():

    brand1 = BrandDto(
        brand_id=1,
        name="HoneyBee",
        min_quantity=2,
        max_quantity=10,
        price_per_item=100
    )
    brand2 = BrandDto(
            brand_id=2,
            name="KnockOut",
            min_quantity=2,
            max_quantity=11,
            price_per_item=200
    )
    
    order1 = GetFormItemOrderDto(order_id=1,
                                 brand_id=1,
                                 ordered_count=10,
                                 out_of_stock=0)
    order2 = GetFormItemOrderDto(order_id=2,
                                 brand_id=3,
                                 ordered_count=10,
                                 out_of_stock=0)
    
    item1 = GetFormItemDto(item_id=1,
                           name="choco",
                           description="choco",
                           brands=[brand1],
                           order=order1)

    

    section1 = GetFormSectionDto(section_id=1,
                                 name="SECTION1",
                                 description="DESCRIP SECTION1",
                                 items=[item1])
    
    get_form_dto = GetFormDto(form_id=1,
                              name="FORM1",
                              close_date=datetime.datetime(2020, 10, 10, 0, 0),
                              sections=[section1])

    return get_form_dto


@pytest.fixture()
def get_form_expected_dict():

    form_dict = {
            "form_id": 1,
            "form_name": "FORM1",
            "close_date": "10th October 12AM",
            "sections": [
                {
                    "section_id": 1,
                    "section_name": "SECTION1",
                    "description": "DESCRIP SECTION1",
                    "items_details": [
                        {
                            "item_id": 1,
                            "item_name": "choco",
                            "description": "choco",
                            "brands": [
                                {
                                    "brand_id": 1,
                                    "brand_name": "HoneyBee",
                                    "min_quantity": 2,
                                    "max_quantity": 10,
                                    "price_per_item": 100
                                }
                            ],
                            "order": {
                                "order_id": 1,
                                "brand_id": 1,
                                "ordered_count": 10,
                                "out_of_stock": 0
                            }
                    }
                    ]
            }
        ]
    }
    return form_dict
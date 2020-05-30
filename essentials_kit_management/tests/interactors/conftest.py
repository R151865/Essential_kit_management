import datetime

import pytest

from essentials_kit_management.interactors.storages.dtos import (
    UserDto, BrandDto, ItemDto, SectionDto, FormDto, OrderDto,
    HomePageFormDto, GetFormBrandDto, GetFormSectionDto, GetFormItemDto,
    GetFormDto, GetSectionItemDto, GetFormItemOrderDto
    )



@pytest.fixture()
def user_dtos():
    user_dtos = [
        UserDto(user_id=1,
                name="sulthan",
                username="123445678",
                password="sulthan@123"),
        UserDto(user_id=2,
                name="anju",
                username="123445671",
                password="anju@123")
        ]
    return user_dtos


@pytest.fixture()
def brand_dtos():
    brand_dtos = [
        BrandDto(brand_id=1,
                 name="HoneyBee",
                 min_quantity=2,
                 max_quantity=10,
                 price_per_item=100),
        BrandDto(brand_id=2,
                 name="KnockOut",
                 min_quantity=2,
                 max_quantity=11,
                 price_per_item=200)
        ]
    return brand_dtos


@pytest.fixture()
def items_dtos():
    items_dtos = [
        ItemDto(item_id=1,
                name="Choco",
                description="choco",
                brand_id=1),
        ItemDto(item_id=2,
                name="lace",
                description="lace",
                brand_id=2)
        ]
    return items_dtos

@pytest.fixture()
def order_dtos():
    order_dtos = [
        OrderDto(order_id=1,
                 user_id=1,
                 item_id=1,
                 brand_id=1,
                 form_id=1,
                 section_id=1,
                 count=10,
                 pending_count=0,
                 out_of_stock=0),
        OrderDto(order_id=2,
                 user_id=2,
                 item_id=2,
                 brand_id=2,
                 form_id=1,
                 section_id=2,
                 count=10,
                 pending_count=5,
                 out_of_stock=0),
        OrderDto(order_id=3,
                 user_id=2,
                 item_id=2,
                 brand_id=2,
                 form_id=2,
                 section_id=2,
                 count=5,
                 pending_count=5,
                 out_of_stock=5)

        ]
    return order_dtos


@pytest.fixture()
def form_dtos():
    form_dtos = [
        FormDto(form_id=1,
                name="FORM1",
                description="FORM1",
                status="LIVE",
                close_date=datetime.datetime(2020,10,10,0,0),
                expected_delivery_date=datetime.datetime(2020,10,10,0,0)),
        FormDto(form_id=2,
                name="FORM2",
                description="FORM2",
                status="CLOSED",
                close_date=datetime.datetime(2020,10,10,0,0),
                expected_delivery_date=datetime.datetime(2020,10,10,0,0)),
        FormDto(form_id=3,
                name="FORM3",
                description="FORM3",
                status="LIVE",
                close_date=datetime.datetime(2020,10,10,0,0),
                expected_delivery_date=datetime.datetime(2020,10,10,0,0))

        ]
    return form_dtos


@pytest.fixture()
def get_expected_form_dtos():
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
                        cost_incurred_for_delivery=0),
        HomePageFormDto(form_id=3,
                        name="FORM3",
                        status="LIVE",
                        close_date=datetime.datetime(2020,10,10,0,0),
                        expected_delivery_date=datetime.datetime(
                            2020,10,10,0,0),
                        items_count=0,
                        estimated_cost=0,
                        items_pending_count=0,
                        cost_incurred_for_delivery=0)

        ]
    return home_page_form_dtos



@pytest.fixture()
def get_form_dto():
    form_dto = FormDto(
        form_id=1,
        name="FORM1",
        description="FORM1",
        status="LIVE",
        close_date=datetime.datetime(2020, 10, 10, 0, 0),
        expected_delivery_date=datetime.datetime(2020, 10, 10, 0, 0)
    )

    return form_dto

@pytest.fixture()
def get_form_order_dtos():
    order_dtos = [
        OrderDto(order_id=1,
                 user_id=1,
                 item_id=1,
                 brand_id=1,
                 form_id=1,
                 section_id=1,
                 count=10,
                 pending_count=0,
                 out_of_stock=0),
        OrderDto(order_id=2,
                 user_id=1,
                 item_id=2,
                 brand_id=2,
                 form_id=1,
                 section_id=1,
                 count=10,
                 pending_count=5,
                 out_of_stock=0)
        ]
    return order_dtos


@pytest.fixture()
def get_form_brand_dtos():
    brand_dtos = [
        GetFormBrandDto(
            brand_id=1,
            name="HoneyBee",
            min_quantity=2,
            max_quantity=10,
            price_per_item=100),
        GetFormBrandDto(
            brand_id=2,
            name="KnockOut",
            min_quantity=2,
            max_quantity=11,
            price_per_item=200)
        ]
    return brand_dtos


@pytest.fixture()
def get_form_section_dtos():

    section_dtos = [
        SectionDto(section_id=1,
                   name="SECTION1",
                   description="DESCRIP SECTION1")
           ]
    return section_dtos



@pytest.fixture()
def get_form_items_dtos():
    items_dtos = [
        ItemDto(item_id=1,
                name="choco",
                description="choco",
                brand_id=1),
        ItemDto(item_id=2,
                name="lace",
                description="lace",
                brand_id=3)
        ]
    return items_dtos


@pytest.fixture()
def get_form_expected_form_details_dto():

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

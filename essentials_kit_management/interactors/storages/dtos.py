import datetime

from dataclasses import dataclass

from typing import Optional, List

from essentials_kit_management.constants.enums import FormStatusEnum


@dataclass
class HomePageFormDto:
    form_id: int
    name: str
    status: FormStatusEnum
    close_date: datetime
    expected_delivery_date: datetime
    items_count: int
    estimated_cost: int
    items_pending_count: int
    cost_incurred_for_delivery: int


@dataclass
class UserDto:
    user_id: int
    name: str
    username: int
    password: str


@dataclass
class BrandDto:
    brand_id: int
    name: str
    min_quantity: int
    max_quantity: int
    price_per_item: int


@dataclass
class ItemDto:
    item_id: int
    name: str
    description: str
    brand_id: int


@dataclass
class  SectionDto:
    section_id: int
    name: str
    description: str


@dataclass
class FormDto:
    form_id: int
    name: str
    description: str
    status: FormStatusEnum
    close_date: datetime
    expected_delivery_date: datetime=None


@dataclass
class OrderDto:
    order_id: int
    user_id: int
    item_id: int
    brand_id: int
    form_id: int
    section_id: int
    count: int
    pending_count: int
    out_of_stock: int


@dataclass
class FormCompleteDetailsDto:
    form_dto: FormDto
    item_dtos: List[ItemDto]
    order_dtos: List[OrderDto]
    brand_dtos: List[BrandDto]


@dataclass
class GetFormItemOrderDto:
    order_id: int
    brand_id: int
    ordered_count: int
    out_of_stock: int


@dataclass
class GetSectionItemDto:
    item_id: int
    name: str
    description: str
    section_id: int


@dataclass
class GetFormItemDto:
    item_id: int
    name: str
    description: str
    brands: List[BrandDto]
    order: GetFormItemOrderDto


@dataclass
class  GetFormSectionDto:
    section_id: int
    name: str
    description: str
    items: List[GetFormItemDto]


@dataclass
class GetFormDto:
    form_id: int
    name: str
    close_date: int
    sections: List[GetFormSectionDto]


@dataclass
class GetFormBrandDto:
    brand_id: int
    name: str
    min_quantity: int
    max_quantity: int
    price_per_item: int
from essentials_kit_management.interactors.storages.form_storage_interface \
    import FormStorageInterface

from typing import List

from essentials_kit_management.models import (
    Form, Order, Brand, Item, Section
)

from essentials_kit_management.interactors.storages.dtos import (
    FormDto, OrderDto, BrandDto, ItemDto, SectionDto, FormCompleteDetailsDto,
)


class FormStorageImplementation(FormStorageInterface):


    def is_valid_form_id(self, form_id: int):
        is_valid_form_id = Form.objects.filter(id=form_id).exists()
        return is_valid_form_id

    def get_forms_dtos(self,
                       offset: int,
                       limit: int) ->List[FormCompleteDetailsDto]:

        form_objs = Form.objects.filter()[offset: offset+limit]
        form_dtos = self._convert_form_objs_to_dtos(form_objs=form_objs)

        return form_dtos

    def _convert_form_objs_to_dtos(self, form_objs) ->List[FormDto]:
        form_dto_list = []

        for form in form_objs:
            dto = self._convert_form_obj_to_dto(form)
            form_dto_list.append(dto)
            
        return form_dto_list

    def _convert_form_obj_to_dto(self, form_obj) ->FormDto:
        return FormDto(
                form_id=form_obj.id,
                name=form_obj.name,
                description=form_obj.description,
                status=form_obj.status,
                close_date=form_obj.close_date,
                expected_delivery_date=form_obj.expected_delivery_date)

    def _convert_order_objs_to_dtos(self, order_objs) ->List[OrderDto]:
        order_dtos_list = []

        for order in order_objs:
            dto = OrderDto(order_id=order.id,
                          user_id=order.user_id,
                          item_id=order.item_id,
                          brand_id=order.brand_id,
                          form_id=order.form_id,
                          section_id=order.section_id,
                          count=order.count,
                          pending_count=order.pending_count,
                          out_of_stock=order.out_of_stock)
            order_dtos_list.append(dto)
        return order_dtos_list

    def _convert_brand_obj_to_dto(self, brand) ->BrandDto:
        return BrandDto(brand_id=brand.id,
                        name=brand.name,
                        min_quantity=brand.min_quantity,
                        max_quantity=brand.max_quantity,
                        price_per_item=brand.price_per_item)

    def _convert_item_obj_to_dto(self, item) ->ItemDto:
        return ItemDto(item_id=item.id,
                       name=item.name,
                       description=item.description,
                       brand_id=item.brand_id)

    def _convert_section_obj_to_dto(self, section_obj) ->SectionDto:
        return SectionDto(section_id=section_obj.id,
                          name=section_obj.name,
                          description=section_obj.description)

    def get_form_to_fill_dto(self, form_id: int):
        pass

    def get_user_order_dtos(self, user_id) ->List[OrderDto]:

        order_objs = Order.objects.filter(user_id=user_id)
        order_dtos = self._convert_order_objs_to_dtos(order_objs)
        return order_dtos

    def get_user_brand_dtos(self, orders) ->List[BrandDto]:

        brand_ids = [order.brand_id for order in orders]
        brand_objs = Brand.objects.filter(id__in=brand_ids)

        brand_dtos = [ 
            self._convert_brand_obj_to_dto(brand)
            for brand in brand_objs
        ]
        return brand_dtos

    def get_user_item_dtos(self, orders) ->List[ItemDto]:
        
        item_ids = [order.item_id for order in orders]
        item_objs = Item.objects.filter(id__in=item_ids)

        item_dtos_list = [
            self._convert_item_obj_to_dto(item)
            for item in item_objs
            ]
        return item_dtos_list

    def get_form_dto(self, form_id: int) ->FormDto:
        form_obj = Form.objects.get(id=form_id)
        return self._convert_form_obj_to_dto(form_obj)

    def get_order_dtos(self, user_id: int, form_id: int):
        order_objs = Order.objects.filter(user_id=user_id,
                                          form_id=form_id)
        order_dtos_list = self._convert_order_objs_to_dtos(order_objs)
        return order_dtos_list

    def get_form_sections_dtos(self, form_id: int) ->List[SectionDto]:
        section_ids = [
            Order.objects.filter(form_id=form_id) \
                 .values_list("section_id", flat=True)]

        section_objs = Section.objects.filter(id__in=section_ids)

        section_dtos_list = [
            self._convert_section_obj_to_dto(section)
            for section in section_objs
            ]
        return section_dtos_list

    def get_item_dtos(self, order_dtos) ->List[ItemDto]:
        item_ids = [order.item_id for order in order_dtos]

        item_objs = Item.objects.filter(id__in=item_ids)

        item_dtos_list = [
            self._convert_item_obj_to_dto(item)
            for item in item_objs
            ]
        return item_dtos_list

    def get_brand_dtos(self, item_dtos) ->List[BrandDto]:

        items_ids = [item.item_id for item in item_dtos]
        brand_ids = list(Order.objects.filter(item_id__in=items_ids) \
                          .values_list("brand_id", flat=True))

        brand_objs = Brand.objects.filter(id__in=brand_ids)

        brand_dtos_list = [
            self._convert_brand_obj_to_dto(brand)
            for brand in brand_objs
        ]
        return brand_dtos_list

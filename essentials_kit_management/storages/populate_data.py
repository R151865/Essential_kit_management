import datetime


from essentials_kit_management.models import (
    User, Item, Brand, Section, Form, Transaction, Order, Account
    )



users_list = [
    {
        "name": "user1",
        "username": "user1123",
        "password": "user1@",
        "is_admin": False
    },
    {
        "name": "user2",
        "username": "user2123",
        "password": "user2@",
        "is_admin": False
    },
    {
        "name": "prudhvi",
        "username": 12345,
        "password": "12345",
        "is_admin": False
    },
    {
        "name": "Admin1",
        "username": "admin1123",
        "password": "admin1@",
        "is_admin": True
    },
    {
        "name": "Admin2",
        "username": "admin2123",
        "password": "admin2@",
        "is_admin": True
    }

    ]

def create_users():
    for user in users_list:
        User.objects.create(name=user["name"],
                           username=user["username"],
                           password=user["password"],
                           is_admin=user["is_admin"])



account_list = [
    {
        "upi_id": "1234567890@SBI"
    }
]

def create_account():
    for account in account_list:
        Account.objects.create(upi_id=account["upi_id"])




forms_details_list = [
    {
        "name": "form1",
        "description": "form1 description",
        "close_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "DONE",
        "sections": [
            {
                "name": "section1", "description": "section1 description",
                "items": [
                    {
                        "name": "item1", "description": "item1 description",
                        "brands": [
                            {
                                "name": "item1 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item1 brand2", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": " item1 brand3", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item2", "description": "item2 description",
                        "brands": [
                            {
                                "name": " item2 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": " item2 brand1", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "item2 brand1", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section2",
                "description": "section2 description",
                "items": [
                    {
                        "name": "item3",
                        "description": "item3 description",
                        "brands": [
                            {
                                "name": "item3 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item3 brand2", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "item3 brand3", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item4",
                        "description": "item4 description",
                        "brands": [
                            {
                                "name": "item4 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item4 brand2", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "item4 brand3", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    
    {
        "name": "form2",
        "description": "form2 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "LIVE",
        "sections": [
            {
                "name": "section3", "description": "section1 description",
                "items": [
                    {
                        "name": "item5", "description": "item1 description",
                        "brands": [
                            {
                                "name": "item5 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item5 brand2", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": " item5 brand3", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item6", "description": "item2 description",
                        "brands": [
                            {
                                "name": " item6 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": " item6 brand1", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "item6 brand1", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section4",
                "description": "section2 description",
                "items": [
                    {
                        "name": "item7",
                        "description": "item7 description",
                        "brands": [
                            {
                                "name": "item7 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item7 brand2", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "item7 brand3", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item8",
                        "description": "item8 description",
                        "brands": [
                            {
                                "name": "item8 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item8 brand2", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "item8 brand3", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },

    {
        "name": "form3",
        "description": "form3 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "LIVE",
        "sections": [
            {
                "name": "section5", "description": "section5 description",
                "items": [
                    {
                        "name": "item9", "description": "item9 description",
                        "brands": [
                            {
                                "name": "item9 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item9 brand2", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": " item9 brand3", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item10", "description": "item10 description",
                        "brands": [
                            {
                                "name": " item10 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": " item10 brand1", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "item10 brand1", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section6",
                "description": "section6 description",
                "items": [
                    {
                        "name": "item11",
                        "description": "item11 description",
                        "brands": [
                            {
                                "name": "item11 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item11 brand2", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "item11 brand3", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item12",
                        "description": "item12 description",
                        "brands": [
                            {
                                "name": "item12 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item12 brand2", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "item12 brand3", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },

    {
        "name": "form4",
        "description": "form4 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": [
            {
                "name": "section7", "description": "section7 description",
                "items": [
                    {
                        "name": "item13", "description": "item13 description",
                        "brands": [
                            {
                                "name": "item13 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item13 brand2", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": " item13 brand3", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item14", "description": "item14 description",
                        "brands": [
                            {
                                "name": " item14 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": " item14 brand1", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "item14 brand1", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                        ]
            },
            {
                "name": "section8",
                "description": "section8 description",
                "items": [
                    {
                        "name": "item15",
                        "description": "item15 description",
                        "brands": [
                            {
                                "name": "item15 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item15 brand2", "min_quantity": 2,
                                "max_quantity": 8, "price_per_item": 200
                            },
                            {
                                "name": "item15 brand3", "min_quantity": 5,
                                "max_quantity": 7, "price_per_item": 50
                            }
                            
                            ]
                    },
                    {
                        "name": "item16",
                        "description": "item16 description",
                        "brands": [
                            {
                                "name": "item16 brand1", "min_quantity": 1, 
                                "max_quantity": 5, "price_per_item": 100
                            },
                            {
                                "name": "item16 brand2", "min_quantity": 2,
                                "max_quantity": 5, "price_per_item": 200
                            },
                            {
                                "name": "item16 brand3", "min_quantity": 2,
                                "max_quantity": 6, "price_per_item": 50
                            }
                            
                            ]
                    }
                    
                    ]
            }
            ]
    },
    # forms with no data
    {
        "name": "form5",
        "description": "form5 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },
    {
        "name": "form6",
        "description": "form6 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },
    {
        "name": "form7",
        "description": "form7 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },{
        "name": "form8",
        "description": "form8 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },{
        "name": "form9",
        "description": "form9 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },{
        "name": "form10",
        "description": "form10 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },{
        "name": "form11",
        "description": "form11 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },{
        "name": "form12",
        "description": "form12 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },{
        "name": "form13",
        "description": "form13 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },
    {
        "name": "form14",
        "description": "form14 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },{
        "name": "form15",
        "description": "form15 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },{
        "name": "form15",
        "description": "form15 description",
        "close_date": datetime.datetime(2020, 10, 8, 0, 0, 0),
        "expected_delivery_date": datetime.datetime(2020, 10, 10, 0, 0, 0),
        "status": "CLOSED",
        "sections": []
    },
]


def populate_data():
    
    create_users()
    create_account()

    for form in forms_details_list:
        form_obj = Form.objects.create(name=form["name"], status=form["status"],
                                       description=form["description"],
                                       close_date=form["close_date"],
                                       expected_delivery_date=form["expected_delivery_date"])

        for section in form["sections"]:
            section_obj = Section.objects.create(name=section["name"],
                                                 description=section["description"])
            form_obj.sections.add(section_obj)

            for item in section["items"]:
                item_obj = Item.objects.create(name=item["name"],
                                               description=item["description"])
                section_obj.items.add(item_obj)

                for brand in item["brands"]:
                    brand_obj = Brand.objects.create(name=brand["name"],
                                                     min_quantity=brand["min_quantity"],
                                                     max_quantity=brand["max_quantity"],
                                                     price_per_item=brand["price_per_item"])
                    item_obj.brand.add(brand_obj)


    create_orders()
    create_transactions()

    print("data populated successfully Hurrah!.......")






order_list = [
    {
         "user_id":1,
         "item_id": 1,
         "brand_id": 1,
         "form_id": 1,
         "section_id": 1,
         "count": 2,
         "pending_count": 0,
         "out_of_stock": 0
     },
     {
         "user_id":1,
         "item_id": 2,
         "brand_id": 4,
         "form_id": 1,
         "section_id": 1,
         "count": 2,
         "pending_count": 0,
         "out_of_stock": 0
     },
     {
         "user_id":1,
         "item_id": 5,
         "brand_id": 15,
         "form_id": 2,
         "section_id": 3,
         "count": 2,
         "pending_count": 0,
         "out_of_stock": 0
     },
     {
         "user_id":1,
         "item_id": 19,
         "brand_id": 25,
         "form_id": 3,
         "section_id": 4,
         "count": 2,
         "pending_count": 0,
         "out_of_stock": 0
     },
# user 2 orders
    {
         "user_id":2,
         "item_id": 1,
         "brand_id": 1,
         "form_id": 1,
         "section_id": 1,
         "count": 2,
         "pending_count": 0,
         "out_of_stock": 0
     },
     {
         "user_id":2,
         "item_id": 2,
         "brand_id": 4,
         "form_id": 1,
         "section_id": 1,
         "count": 2,
         "pending_count": 0,
         "out_of_stock": 0
     },
     {
         "user_id":2,
         "item_id": 5,
         "brand_id": 15,
         "form_id": 2,
         "section_id": 3,
         "count": 2,
         "pending_count": 0,
         "out_of_stock": 0
     },
     {
         "user_id":2,
         "item_id": 19,
         "brand_id": 25,
         "form_id": 3,
         "section_id": 4,
         "count": 2,
         "pending_count": 0,
         "out_of_stock": 0
     }
]

def create_orders():
    order_objs = [
            Order.objects.create(user_id=order["user_id"],
                  item_id=order["item_id"],
                  brand_id=order["brand_id"],
                  form_id=order["form_id"],
                  section_id=order["section_id"],
                  count=order["count"],
                  pending_count=order["pending_count"],
                  out_of_stock=order["out_of_stock"]
                )
            for order in order_list
            ]
    return order_objs



transaction_list = [
    {
        "transaction_id": 1,
        "user_id": 1,
        "amount": 1000,
        "status": "APPROVED",
        "transaction_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 2,
        "user_id": 1,
        "amount": -500,
        "status": "APPROVED",
        "transaction_type": "PHONE_PAY",
        "screen_shot": "",
        "remark": "form1"
    },
    {
        "transaction_id": 3,
        "user_id": 1,
        "amount": 200,
        "status": "REJECTED",
        "transaction_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },

    # user 2 transactions
    {
        "transaction_id": 4,
        "user_id": 2,
        "amount": 1000,
        "status": "APPROVED",
        "transaction_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    },
    {
        "transaction_id": 5,
        "user_id": 2,
        "amount": -500,
        "status": "APPROVED",
        "transaction_type": "PHONE_PAY",
        "screen_shot": "",
        "remark": "form1"
    },
    {
        "transaction_id": 6,
        "user_id": 2,
        "amount": 200,
        "status": "REJECTED",
        "transaction_type": "PHONE_PAY",
        "screen_shot": "screen_shot/payment.png",
        "remark": "wallet"
    }
]

def create_transactions():

    for transaction in transaction_list:
        Transaction.objects.create(
            transaction_id=transaction['transaction_id'],
            user_id=transaction['user_id'],
            amount=transaction['amount'],
            status=transaction['status'],
            transaction_type=transaction["transaction_type"],
            screen_shot=transaction["screen_shot"],
            remark=transaction["remark"])


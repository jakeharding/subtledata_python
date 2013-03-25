#!/usr/bin/env python
"""
Copyright 2012 Wordnik, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class OpenTicket:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'employee_id': 'int',
            'user_id': 'int',
            'number_of_guests': 'int',
            'items': 'list[Item]',
            'tax': 'float',
            'discount': 'float',
            'pos_ticket_id': 'int',
            'remaining_balance': 'float',
            'table_id': 'int',
            'ticket_id': 'int',
            'date_opened': 'str',
            'table_name': 'str',
            'total': 'float',
            'subtotal': 'float',
            'service_charge': 'float'

        }


        #Employee ID
        self.employee_id = None # int
        #User ID
        self.user_id = None # int
        #Number of guests on ticket
        self.number_of_guests = None # int
        self.items = None # list[Item]
        #Tax amount
        self.tax = None # float
        #Discount amount
        self.discount = None # float
        #POS System Ticket Identifier
        self.pos_ticket_id = None # int
        #Ticket remaining balance
        self.remaining_balance = None # float
        #Table ID
        self.table_id = None # int
        #Ticket ID
        self.ticket_id = None # int
        #Date/Time Ticket Opened
        self.date_opened = None # str
        #Table Name
        self.table_name = None # str
        #Total amount
        self.total = None # float
        #Subtotal amount
        self.subtotal = None # float
        #Service charge
        self.service_charge = None # float
        
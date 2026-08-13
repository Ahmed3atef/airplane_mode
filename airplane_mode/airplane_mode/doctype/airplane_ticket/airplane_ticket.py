# Copyright (c) 2026, ahmed.atef and contributors
# For license information, please see license.txt

import random
import frappe
from frappe.model.document import Document
from frappe.utils import flt


class AirplaneTicket(Document):
    def before_insert(self):
        if not self.seat:
            self.seat = get_random_seat()

    def validate(self):
        validate_add_ons(self.get("add_ons"))

    def before_save(self):
        total_addons = 0
        for i in self.add_ons:
            total_addons += flt(i.amount)

        self.flight_price = flt(self.flight_price or 10000)
        self.total_amount = self.flight_price + total_addons

    def before_submit(self):
        validate_status_on_submit(self.status)

    def on_submit(self):
        self.status = "Checked-In"

    def on_cancel(self):
        self.status = "Boarded"


def validate_status_on_submit(status):
    if status != "Boarded":
        frappe.throw("Status must be Boarded to submit ")


def get_random_seat():
    return f"{random.randint(1, 99)}{random.choice('ABCDE')}"


def validate_add_ons(itmes):
    add_ons = set()
    
    for row in itmes:
        if row.item in add_ons:
            frappe.throw(
                (f"Row #{row.idx}: Add On {frappe.bold(row.item)} already exists")
            )
        add_ons.add(row.item)
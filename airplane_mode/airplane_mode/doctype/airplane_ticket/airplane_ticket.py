# Copyright (c) 2026, ahmed.atef and contributors
# For license information, please see license.txt

import random
import frappe
from frappe.model.document import Document
from frappe.utils import flt


class AirplaneTicket(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import AirplaneTicketAddonItem
        from frappe.types import DF

        add_ons: DF.Table[AirplaneTicketAddonItem]
        amended_from: DF.Link | None
        departure_date: DF.Date | None
        departure_time: DF.Time | None
        destination_airport_code: DF.Data | None
        duration_of_flight: DF.Duration | None
        flight: DF.Link | None
        flight_price: DF.Currency
        passenger: DF.Link | None
        seat: DF.Data | None
        source_airport_code: DF.Data | None
        status: DF.Literal["", "Booked", "Checked-In", "Boarded"]
        total_amount: DF.Currency
    # end: auto-generated types

    def before_insert(self) -> None:
        self.validate_flight_capacity()
        if not self.seat:
            self.seat = self.get_random_seat()

    def validate(self) -> None:
        self.validate_add_ons(self.get("add_ons"))

    def before_save(self) -> None:
        total_addons = 0
        for i in self.add_ons:
            total_addons += flt(i.amount)

        self.flight_price = flt(self.flight_price or 10000)
        self.total_amount = self.flight_price + total_addons

    def before_submit(self) -> None:
        self.validate_status_on_submit(self.status)

    def on_submit(self) -> None:
        self.status = "Checked-In"

    def on_cancel(self) -> None:
        self.status = "Boarded"


    def validate_status_on_submit(self, status: str) -> None:
        if status != "Boarded":
            frappe.throw("Status must be Boarded to submit ")

    def validate_flight_capacity(self) -> None:
        airplane = frappe.db.get_value("Airplane Flight", self.flight, "airplane")
        capacity = frappe.db.get_value("Airplane", airplane, "capacity")
        ticket_count = frappe.db.count(
            "Airplane Ticket",
            {
                "flight": self.flight,
                "docstatus" : ["!=",2]
            }
        )
        
        if ticket_count >= capacity:
            frappe.throw("No seats are available for this flight.")


    def get_random_seat(self) -> str:
        return f"{random.randint(1, 99)}{random.choice('ABCDE')}"


    def validate_add_ons(self, itmes) -> None:
        add_ons = set()
        
        for row in itmes:
            if row.item in add_ons:
                frappe.throw(
                    (f"Row #{row.idx}: Add On {frappe.bold(row.item)} already exists")
                )
            add_ons.add(row.item)
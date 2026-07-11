import random

import frappe
from frappe.qb import DocType


def execute():
    populate_missing_seats()


def populate_missing_seats():
    airplane_ticket = DocType("Airplane Ticket")
    tickets = (
        frappe.qb.from_(airplane_ticket)
        .select(airplane_ticket.name)
        .where((airplane_ticket.seat == "") | (airplane_ticket.seat.isnull()))
        .run(as_dict=True)
    )

    for ticket in tickets:
        frappe.db.set_value(
            "Airplane Ticket",
            ticket.name,
            "seat",
            get_random_seat(),
            update_modified=False,
        )

    if tickets:
        frappe.db.commit()


def get_random_seat():
    return f"{random.randint(1, 99)}{random.choice('ABCDE')}"

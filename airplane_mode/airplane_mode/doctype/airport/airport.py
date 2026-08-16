# Copyright (c) 2026, ahmed.atef and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Airport(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		city: DF.Data | None
		code: DF.Data | None
		country: DF.Data | None
	# end: auto-generated types

	pass

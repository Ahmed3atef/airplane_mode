# Copyright (c) 2026, ahmed.atef and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Airplane(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airline: DF.Link | None
		capacity: DF.Int
		model: DF.Data | None
	# end: auto-generated types

	pass

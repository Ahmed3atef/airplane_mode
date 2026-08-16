# Copyright (c) 2026, ahmed.atef and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date_of_birth: DF.Date | None
		first_name: DF.Data | None
		full_name: DF.Data | None
		last_name: DF.Data | None
	# end: auto-generated types

	def before_save(self) -> None:
		self.full_name = f"{self.first_name or ''} {self.last_name or ''}"

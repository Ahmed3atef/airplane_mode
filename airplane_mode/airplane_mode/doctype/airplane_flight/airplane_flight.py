# Copyright (c) 2026, ahmed.atef and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airplane: DF.Link | None
		amended_from: DF.Link | None
		date_of_departure: DF.Date | None
		destination_airport: DF.Link | None
		destination_airport_code: DF.Data | None
		duration: DF.Duration | None
		is_published: DF.Check
		route: DF.Data | None
		source_airport: DF.Link | None
		source_airport_code: DF.Data | None
		status: DF.Literal["", "Scheduled", "Completed", "Cancelled"]
		time_of_departure: DF.Time | None
	# end: auto-generated types

	def on_submit(self) -> None:
		self.status = "Completed"

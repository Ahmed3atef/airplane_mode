import frappe
from frappe.query_builder.functions import Count


def execute(filters=None):
	columns = get_columns()
	data = get_data()
	return columns, data


def get_columns():
	return [
		{
			"label": "Add-on Type",
			"fieldtype": "Link",
			"fieldname": "item",
			"options": "Airplane Ticket Add-on Type",
			"width": 200,
		},
		{
			"label": "Sold Count",
			"fieldtype": "Int",
			"fieldname": "sold_count",
			"width": 150,
		},
	]


def get_data():
	AddOnItem = frappe.qb.DocType("Airplane Ticket Add-on Item")

	data = (
		frappe.qb.from_(AddOnItem)
		.select(AddOnItem.item, Count(AddOnItem.item).as_("sold_count"))
		.groupby(AddOnItem.item)
		.orderby(Count(AddOnItem.item), order=frappe.qb.desc)
	).run(as_dict=True)

	return data

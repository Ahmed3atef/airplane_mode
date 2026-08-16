import frappe
from frappe.query_builder.functions import Sum


def execute(filters=None):
	columns = get_columns()
	data = get_data()
	chart = get_chart(data)
	report_summary = get_report_summary(data)
	return columns, data, None, chart, report_summary


def get_columns():
	return [
		{
			"label": "Airline",
			"fieldtype": "Link",
			"fieldname": "airline",
			"options": "Airline",
			"width": 200,
		},
		{
			"label": "Revenue",
			"fieldtype": "Currency",
			"fieldname": "revenue",
			"width": 150,
		},
	]


def get_data():
	Airline = frappe.qb.DocType("Airline")
	Airplane = frappe.qb.DocType("Airplane")
	Flight = frappe.qb.DocType("Airplane Flight")
	Ticket = frappe.qb.DocType("Airplane Ticket")

	data = (
		frappe.qb.from_(Airline)
		.left_join(Airplane)
		.on(Airplane.airline == Airline.name)
		.left_join(Flight)
		.on(Flight.airplane == Airplane.name)
		.left_join(Ticket)
		.on((Ticket.flight == Flight.name) & (Ticket.docstatus == 1))
		.select(Airline.name.as_("airline"), Sum(Ticket.total_amount).as_("revenue"))
		.groupby(Airline.name)
		.orderby(Sum(Ticket.total_amount), order=frappe.qb.desc)
	).run(as_dict=True)

	for d in data:
		d.revenue = d.revenue or 0

	return data


def get_chart(data):
	return {
		"data": {
			"labels": [d.airline for d in data],
			"datasets": [{"values": [d.revenue for d in data]}],
		},
		"type": "donut",
	}


def get_report_summary(data):
	total = sum(d.revenue for d in data)
	return [
		{
			"value": total,
			"label": "Total Revenue",
			"indicator": "Green",
		}
	]

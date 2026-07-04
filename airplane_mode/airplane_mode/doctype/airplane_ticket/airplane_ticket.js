// Copyright (c) 2026, ahmed.atef and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {

	},
});

frappe.listview_settings["Airplane Ticket"] = {
    has_indicator_for_draft: true,
    has_indicator_for_submit: true,
    has_indicator_for_cancelled: true,
};
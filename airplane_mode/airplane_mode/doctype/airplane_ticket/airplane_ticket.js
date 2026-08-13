// Copyright (c) 2026, ahmed.atef and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        frm.add_custom_button(__("Assign Seat"), ()=>{
            const dialog = new frappe.ui.Dialog({
                title: __("Assign Seat"),
                fields: [
                    {
                        label: __("Seat Number"),
                        fieldname: "seat",
                        fieldtype: "Data",
                        reqd: 1,
                    }
                ],
                primary_action_label: __("Assing"),
                primary_action(values){
                    frm.set_value("seat", values.seat);
                    dialog.hide();
                },
            });
            dialog.show();
        },__("Actions"));
    },
});

frappe.listview_settings["Airplane Ticket"] = {
    has_indicator_for_draft: true,
    has_indicator_for_submit: true,
    has_indicator_for_cancelled: true,
};
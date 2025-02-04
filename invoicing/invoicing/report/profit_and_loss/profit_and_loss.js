// Copyright (c) 2025, Ahmed Emam and contributors
// For license information, please see license.txt

// frappe.query_reports["Profit and Loss"] = {
// 	"filters": [

// 	]
// };

frappe.query_reports["Profit and Loss"] = $.extend({}, erpnext.financial_statements);

erpnext.utils.add_dimensions("Profit and Loss", 10);

frappe.query_reports["Profit and Loss"]["filters"].push({
	fieldname: "selected_view",
	label: __("Select View"),
	fieldtype: "Select",
	options: [
		{ value: "Report", label: __("Report View") },
		{ value: "Growth", label: __("Growth View") },
		{ value: "Margin", label: __("Margin View") },
	],
	default: "Growth",
	reqd: 1,
});

frappe.query_reports["Profit and Loss"]["filters"].push({
	fieldname: "accumulated_values",
	label: __("Accumulated Values"),
	fieldtype: "Check",
	default: 1,
});

frappe.query_reports["Profit and Loss"]["filters"].push({
	fieldname: "include_default_book_entries",
	label: __("Include Default FB Entries"),
	fieldtype: "Check",
	default: 1,
});

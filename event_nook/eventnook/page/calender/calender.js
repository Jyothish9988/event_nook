frappe.pages['calender'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Calender',
		single_column: true
	});
}
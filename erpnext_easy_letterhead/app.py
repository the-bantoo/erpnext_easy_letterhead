import frappe


def verify_letterhead(lh, method):
	if lh.easy_mode == 1:
		frappe.db.set_value('Letter Head', lh.name, 'source', 'HTML')
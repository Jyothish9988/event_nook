# Copyright (c) 2024, Jyothish S L and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "room_no", "label": "Room No", "fieldtype": "Link", "options": "Rooms"},
        {"fieldname": "user_id", "label": "User Id", "fieldtype": "Link", "options": "Userlist"},
        {"fieldname": "date", "label": "Date", "fieldtype": "Date"},
        {"fieldname": "time_from", "label": "Time From", "fieldtype": "Select"},
        {"fieldname": "time_to", "label": "Time To", "fieldtype": "Select"},
        {"fieldname": "details", "label": "Details", "fieldtype": "Data"},
        {"fieldname": "expected_capacity", "label": "Expected Capacity", "fieldtype": "Data"},
        {"fieldname": "amended_from", "label": "Amended From", "fieldtype": "Link", "options": "Bookings"},
        {"fieldname": "projector", "label": "Projector", "fieldtype": "Check"},
        {"fieldname": "white_board", "label": "White Board", "fieldtype": "Check"},
        {"fieldname": "audio_system", "label": "Audio System", "fieldtype": "Check"},
        {"fieldname": "video_network_system", "label": "Video Network System", "fieldtype": "Check"}
    ]

    conditions = ""
    if filters.get("date"):
        conditions += f" AND date = '{filters.get('date')}'"
    if filters.get("room_no"):
        conditions += f" AND room_no = '{filters.get('room_no')}'"

    data = frappe.get_all("Bookings", filters=conditions, fields=["*"])

    return columns, data

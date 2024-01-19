# Assuming you have a custom DocType named Bookings

import frappe
from frappe.model.document import Document
from frappe import _

class Bookings(Document):
    def validate(self, method=None):
        # Check room availability before saving the booking
        if self.is_booking_overlapping():
            frappe.throw(_("Room is already booked for the specified date and time range."))

    def is_booking_overlapping(self):
        # Query existing bookings for the specified room and date
        existing_bookings = frappe.get_all("Bookings",
            filters={
                "room_no": self.room_no,
                "date": self.date,
                "name": ("!=", self.name) if self.name else None  # Exclude current booking for updates
            },
            fields=["name", "time_from", "time_to"]
        )

        # Convert current booking time to comparable format (assuming HH:mm:ss)
        current_time_from = frappe.utils.get_time(self.time_from)
        current_time_to = frappe.utils.get_time(self.time_to)

        # Check for overlapping time ranges
        for booking in existing_bookings:
            existing_time_from = frappe.utils.get_time(booking.time_from)
            existing_time_to = frappe.utils.get_time(booking.time_to)

            if (existing_time_from <= current_time_to and existing_time_to >= current_time_from):
                # There is an overlap, room is already booked
                return True

        # No overlapping bookings, room is available
        return False

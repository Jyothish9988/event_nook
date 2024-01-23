from frappe.model.document import Document
import frappe

class Bookings(Document):
    def on_submit(self):
        self.validate_booking_time()

    def validate_booking_time(self):
        # Check if the room is available for the given date and time period
        booked_rooms = frappe.get_all(
            "Bookings",
            filters={
                "room_no": self.room_no,
                "docstatus": 1,
                "name": ("!=", self.name),
                "date": self.date,
                "time_from": ("<", self.time_to),
                "time_to": (">", self.time_from)
            },
        )

        if booked_rooms:
            frappe.throw("The room is already booked for the selected date and time period.")

# Copyright (c) 2026, AssemBahnasy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.naming import make_autoname
from frappe.model.document import Document


class AirplaneTicket(Document):
    def autoname(self):
        self.name = make_autoname(
            f"{self.flight}-{self.source_airport_code}-{self.destination_airport_code}-.###")

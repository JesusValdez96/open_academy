from odoo import fields, models


class AddAttendeeSessions(models.TransientModel):
    _name = "add.attendee.sessions"
    _description = "Add attendees for sessions"

    session_ids = fields.Many2many("session", required=True, default=lambda self: self._context.get('active_ids'))
    attendee_ids = fields.Many2many("res.partner")

    def add_attendees(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'session'
    _description = 'Open Academy Session'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    start_date = fields.Date(default=lambda self: fields.Date.today())
    duration = fields.Float()
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one(
        "res.partner",
        domain=['|',
                ('is_instructor', '=', True),
                ('teacher_level', '!=', False)],
    )
    course_id = fields.Many2one("course", required=True)
    attendee_ids = fields.Many2many("res.partner", string="Attendees")
    taken_seats = fields.Integer(compute="_compute_taken_seats", store=True)

    @api.depends("number_of_seats", "attendee_ids")
    def _compute_taken_seats(self):
        for record in self:
            taken_seats = 0
            if record.number_of_seats > 0:
                taken_seats = len(record.attendee_ids) * 100 / record.number_of_seats
            record.taken_seats = taken_seats

    @api.onchange("number_of_seats", "attendee_ids")
    def onchange_seats(self):
        if self.number_of_seats < 0:
            return {
                "warning": {
                    "title": _("Warning"),
                    "message": _("Number of seats cannot be negative")
                }
            }
        if self.number_of_seats < len(self.attendee_ids):
            return {
                "warning": {
                    "title": _("Warning"),
                    "message": _("Number of attendees exceeds the number of seats")
                }
            }

    @api.constrains("attendee_ids")
    def _check_instructor(self):
        for record in self:
            if record.instructor_id in record.attendee_ids:
                raise ValidationError(_("The instructor cannot be an attendee"))

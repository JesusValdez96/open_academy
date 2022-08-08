from odoo import models, fields, api


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

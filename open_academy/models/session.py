from odoo import models, fields


class Session(models.Model):
    _name = 'session'
    _description = 'Open Academy Session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float()
    number_of_seats = fields.Integer()

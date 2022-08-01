from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Open Academy Course'

    name = fields.Char(required=True)
    description = fields.Text()
    responsible_user = fields.Many2one("res.users")
    sessions = fields.One2many("session", "course")

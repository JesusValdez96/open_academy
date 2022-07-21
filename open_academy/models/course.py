from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Open Academy Course'

    title = fields.Char(required=True)
    description = fields.Text()

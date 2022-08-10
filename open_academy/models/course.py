from odoo import _, fields, models


class Course(models.Model):
    _name = 'course'
    _description = 'Open Academy Course'

    name = fields.Char(required=True)
    description = fields.Text()
    responsible_user_id = fields.Many2one("res.users")
    session_ids = fields.One2many(
        "session",
        "course_id",
        string="Sessions"
    )

    _sql_constraints = [
        (
            "different_title_description",
            "check(name != description)",
            "Description cannot be equal to the course name"
        ),
        (
            "unique_name",
            "unique(name)",
            "Course name must be unique"
        ),
    ]

    def copy(self, default=None):
        default = default or {}
        default.update({
            "name": _("Copy of %s") % self.name,
        })
        return super().copy(default=default)

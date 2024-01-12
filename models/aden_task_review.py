from odoo import fields, models


class TaskReview(models.Model):
    _name = "aden_project.task_review"
    _description = "Task review"

    name = fields.Char(string="Review", size=24, required=True)
    date_of_review = fields.Datetime(string='Fecha revision', index=True, copy=False, tracking=True)
    state_of_review = fields.Selection(
        selection=[
            ("in_review", "En Revision"),
            ("approved", "Aprobado"),
            ("rejected", "Rechazado"),
        ], string="Estado de revision", default="in_review", tracking=True
    ),
    commentary = fields.Text(string="Comentarios"),
    # TODO

from odoo import fields, models


class TaskReview(models.Model):
    _name = "aden_project.task_review"
    _description = "Task review"

    name = fields.Char(string="Nombre", required=True)
    date_of_review = fields.Datetime(string='Fecha', index=True, copy=False)
    state_of_review = fields.Selection(
        selection=[
            ("in_review", "En Revisión"),
            ("approved", "Aprobado"),
            ("rejected", "Rechazado"),
        ], string="Estado", default="in_review"
    )
    commentary = fields.Text(string="Comentarios")
    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Tarea",
        required=True,
        readonly=True,
    )
    # task_reviewer = fields.Many2one(
    #     comodel_name='res.users',
    #     string="Revisor de Codigo"
    # )

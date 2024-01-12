from odoo import fields, models


class CodeReview(models.Model):
    _name = "aden_project.code_review"
    _description = """
    Seccion de code review para las tareas project.task para el sistema de proyectos de ADEN
    """

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


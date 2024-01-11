from odoo import fields, models


class SubCategory(models.Model):
    _name = "aden_project.subcategory"
    _description = "Adding sub-categories to the task for the project system"

    name = fields.Char(string="Sub-Categoria")
    activa = fields.Boolean(string="Activa", default=True, required=True,)

    category_id = fields.Many2one(
        comodel_name="aden_project.category",
        string="Categoria",
        required=True,
    )

    description = fields.Text(string="Descripcion")

    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name="subcategory_id",
        string='Tasks',
        readonly=True,
    )

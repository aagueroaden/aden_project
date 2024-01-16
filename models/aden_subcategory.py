from odoo import fields, models


class SubCategory(models.Model):
    _name = "aden_project.subcategory"
    _description = "Task sub-category"

    name = fields.Char(string="Sub-Categoría")
    active = fields.Boolean(string="Activa", default=True, required=True,)

    category_id = fields.Many2one(
        comodel_name="aden_project.category",
        string="Categoría",
        required=True,
    )

    description = fields.Text(string="Descripción")

    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name="subcategory_id",
        string='Tareas',
        readonly=True,
    )

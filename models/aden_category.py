from odoo import fields, models


class Category(models.Model):
    _name = "aden_project.category"
    _description = "Task Category"

    name = fields.Char(string="Categoría", required=True,)
    description = fields.Text(string="Descripción", required=True,)
    active = fields.Boolean(string="Activo", default=True, required=True,)

    subcategory_ids = fields.One2many(
        comodel_name='aden_project.subcategory',
        inverse_name="category_id",
        string="Sub-Categorías",
        readonly=True,
    )

    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name="category_id",
        string='Tareas',
        readonly=True,
    )

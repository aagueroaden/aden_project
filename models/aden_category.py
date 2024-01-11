from odoo import fields, models


class Category(models.Model):
    _name = "aden_project.category"
    _description = "Adding categories to the task for the project system"

    name = fields.Char(string="Categoria", required=True,)
    description = fields.Text(string="Descripcion", required=True,)
    activa = fields.Boolean(string="Activa", default=True, required=True,)

    subcategory_ids = fields.One2many(
        comodel_name='aden_project.subcategory',
        inverse_name="category_id",
        string="Sub-Categorias",
        readonly=True,
    )

    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name="category_id",
        string='Tasks',
        readonly=True,
    )

from odoo import fields, models


class Resource(models.Model):
    _name = "aden_project.resource"
    _description = "Task Resource"

    name = fields.Char(
        string="Nombre",
        required=True,
    )

    description = fields.Char(
        string="Descripción",
        required=True,
    )

    reference_link = fields.Char(
        string="Url",
        help='Ingresa una Url',
        required=True,
    )

    # ondelete="cascade" when you delete the task,
    # the resource associated with that task are deleted also
    task_id = fields.Many2one(
        string="Recursos",
        comodel_name="project.task",
        readonly=True,
        ondelete="cascade",
    )

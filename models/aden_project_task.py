from odoo import models, fields, api
from odoo.exceptions import ValidationError

WARNING_MSG_NO_TEAM = "no esta asociado a un equipo, asegurese de que este agregado a uno"
WARNING_MSG_TITLE_NO_TEAM = 'Usuario sin equipo!'


class AdenTask(models.Model):
    _inherit = 'project.task'

    task_priority = fields.Selection(selection=[
        ('5', '5 [Muy Baja]'),
        ('4', '4 [Baja]'),
        ('3', '3 [Media]'),
        ('2', '2 [Alta]'),
        ('1', '1 [Muy Alta]'),
        ('0', '0 [Urgente]'),
    ], string='Prioridad', default='5')

    team_id = fields.Many2one(
        comodel_name="aden_project.team",
        string="Equipo asignado",
    )

    resource_ids = fields.One2many(
        comodel_name='aden_project.resource',
        inverse_name="task_id",
        string='Recursos',
    )

    category_id = fields.Many2one(
        comodel_name="aden_project.category",
        string="Categoría"
    )

    subcategory_id = fields.Many2one(
        comodel_name="aden_project.subcategory",
        string="Sub-Categoría"
    )

    task_review_ids = fields.One2many(
        comodel_name="aden_project.task_review",
        inverse_name="task_id",
        string="Revisiones de código",
    )

    @api.constrains('user_ids')
    def _onchange_user_ids_add_remove_team_id(self):
        # need to make a "for task in self", to also work in the kanban/list views
        for task in self:
            for user in task.user_ids:

                # if the user does not have a team assigned
                if not user.team_id:

                    raise ValidationError(
                        f"{WARNING_MSG_TITLE_NO_TEAM}\n{user.name} {WARNING_MSG_NO_TEAM}"
                    )

                # if the task does not have a team assigned, assign the team of the user
                if not task.team_id:
                    task.team_id = user.team_id

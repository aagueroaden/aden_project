from odoo import models, fields, api

WARNING_MSG_NO_TEAM = "este usuario no esta asociado a un equipo, asegurate de agregarlo a uno"
WARNING_MSG_TITLE_NO_TEAM = 'Usuario sin equipo!'


class AdenTask(models.Model):
    _inherit = 'project.task'

    prioridad = fields.Selection(selection=[
        ('5', '5 [Muy Baja]'),
        ('4', '4 [Baja]'),
        ('3', '3 [Media]'),
        ('2', '2 [Alta]'),
        ('1', '1 [Muy Alta]'),
        ('0', '0 [Urgente]'),
    ], string='Prioridad', default='5', tracking=True)

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

    @api.onchange('user_ids')
    def _onchange_user_ids_add_remove_team_id(self):
        # need to make a "for task in self", to also work in the kanban/list views
        for task in self:

            if task.user_ids:
                # take the first user of the user_ids task
                first_user = task.user_ids[0]

                if not first_user.team_id:
                    task.user_ids = False
                    # shows a pop up error
                    return {
                        'warning': {
                            'title': WARNING_MSG_TITLE_NO_TEAM,
                            'message': f"{first_user.name} {WARNING_MSG_NO_TEAM}"}
                    }
                # assign the user team to the task
                task.team_id = first_user.team_id

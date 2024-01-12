from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    team_id = fields.Many2one(
        comodel_name="aden_project.team",
        string="Equipo"
    )


class Team(models.Model):
    _name = "aden_project.team"
    _description = "Project team"

    name = fields.Char(string='Nombre', required=True)
    team_area = fields.Char(string='Área', required=True)

    project_ids = fields.One2many(
        comodel_name='project.project',
        inverse_name="team_id",
        string='Projectos',
        readonly=True
    )

    user_ids_members = fields.One2many(
        comodel_name='res.users',
        inverse_name="team_id",
        string='Integrantes',
        help='Integrantes del Equipo',
        readonly=True
    )

    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name="team_id",
        string='Tareas',
        readonly=True
    )

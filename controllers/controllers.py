# -*- coding: utf-8 -*-
# from odoo import http


# class AdenProject(http.Controller):
#     @http.route('/aden_project/aden_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aden_project/aden_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aden_project.listing', {
#             'root': '/aden_project/aden_project',
#             'objects': http.request.env['aden_project.aden_project'].search([]),
#         })

#     @http.route('/aden_project/aden_project/objects/<model("aden_project.aden_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aden_project.object', {
#             'object': obj
#         })


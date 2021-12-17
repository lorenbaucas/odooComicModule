# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo790(http.Controller):
#     @http.route('/odoo790/odoo790/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo790/odoo790/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo790.listing', {
#             'root': '/odoo790/odoo790',
#             'objects': http.request.env['odoo790.odoo790'].search([]),
#         })

#     @http.route('/odoo790/odoo790/objects/<model("odoo790.odoo790"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo790.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
from odoo import http

# class Hidemenu(http.Controller):
#     @http.route('/hidemenu/hidemenu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hidemenu/hidemenu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hidemenu.listing', {
#             'root': '/hidemenu/hidemenu',
#             'objects': http.request.env['hidemenu.hidemenu'].search([]),
#         })

#     @http.route('/hidemenu/hidemenu/objects/<model("hidemenu.hidemenu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hidemenu.object', {
#             'object': obj
#         })
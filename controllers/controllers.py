# -*- coding: utf-8 -*-
from odoo import http

# class Optativas(http.Controller):
#     @http.route('/optativas/optativas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/optativas/optativas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('optativas.listing', {
#             'root': '/optativas/optativas',
#             'objects': http.request.env['optativas.optativas'].search([]),
#         })

#     @http.route('/optativas/optativas/objects/<model("optativas.optativas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('optativas.object', {
#             'object': obj
#         })
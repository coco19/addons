# -*- coding: utf-8 -*-
from openerp import http

# class Farmacia(http.Controller):
#     @http.route('/farmacia/farmacia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/farmacia/farmacia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('farmacia.listing', {
#             'root': '/farmacia/farmacia',
#             'objects': http.request.env['farmacia.farmacia'].search([]),
#         })

#     @http.route('/farmacia/farmacia/objects/<model("farmacia.farmacia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('farmacia.object', {
#             'object': obj
#         })
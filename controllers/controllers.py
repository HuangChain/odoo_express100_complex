# -*- coding: utf-8 -*-
from odoo import http

# class Kuaidi(http.Controller):
#     @http.route('/kuaidi/kuaidi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kuaidi/kuaidi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kuaidi.listing', {
#             'root': '/kuaidi/kuaidi',
#             'objects': http.request.env['kuaidi.kuaidi'].search([]),
#         })

#     @http.route('/kuaidi/kuaidi/objects/<model("kuaidi.kuaidi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kuaidi.object', {
#             'object': obj
#         })
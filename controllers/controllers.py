# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class VitPortofolio(http.Controller):

	# <model("hr.employee"):employee_id> = parameter id employee
	# @http.route("/portofolio/<model('hr.employee'):employee_id>", auth='public')

	# Public
	@http.route("/portofolio/<int:employee_id>", auth='public')
	def index(self, employee_id, **kw): # hasil parsing di masukan ke fungsi
		employee_id = request.env['hr.employee'].sudo().search([('id', '=', employee_id) ]) # employee_id dari parameter
		
		if employee_id:
			return request.render("vit_portofolio.index", {
				'employee_id'	: employee_id,
			})
		else:
			return request.render("vit_portofolio.not_found", {
			})
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class VitPortofolio(http.Controller):

	# <model("hr.employee"):employee_id> = parameter id employee
	# @http.route("/portofolio/<model('hr.employee'):employee_id>", auth='public')

	# Public Home
	@http.route("/home", auth='public')
	def home(self, **kw):
		employee = request.env['hr.employee'].sudo().search([('id', '!=', None)])

		return request.render("vit_portofolio.home", {
			'employees'	: employee,
		})



	# Public Portofolio
	@http.route("/portofolio/<int:employee_id>", auth='public')
	def portofolio(self, employee_id, **kw): # hasil parsing di masukan ke fungsi
		employee_id = request.env['hr.employee'].sudo().search([('id', '=', employee_id) ]) # employee_id dari parameter
		
		if employee_id:
			return request.render("vit_portofolio.portofolio", {
				'employee_id'	: employee_id,
			})
		else:
			return request.render("vit_portofolio.not_found", {
			})
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class comic(models.Model):
	_name = 'odoo790.comic'
	_description = 'model comic'

	name = fields.Char('ID',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	editorial = fields.Char(string='Editorial',required=True)
	ano_publicacion = fields.Char(string='Año publicacion',required=True)

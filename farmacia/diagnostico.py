# -*- coding: utf-8 -*-

from openerp import fields, models

class Diagnostico (models.Model):
    
    _name = 'farmacia.diagnostico'
    
    codigo = fields.Integer(string = "Codigo")
    descripcion = fields.Text(string = "Descripcion")
    codifica = fields.Many2one('farmacia.capitulo')
# -*- coding: utf-8 -*-

from openerp import models, fields

class capitulo(models.Model):
    _name = 'farmacia.capitulo'
    
    numero = fields.Integer(string="Numero de capitulo")
    titulo = fields.Char(string="Titulo")
    descripcion = fields.Text(string="Descripción")
    organiza_clasificador = fields.Many2one('farmacia.clasificador_enfermedades')
    codificado_en = fields.One2many('farmacia.diagnostico', 'codifica')
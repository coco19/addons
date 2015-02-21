# -*- coding: utf-8 -*-

from openerp import models, fields

class Afiliacion(models.Model):
    _name = 'farmacia.afiliacion'
    
    name = fields.Integer(string="Numero afiliado")
    fecha_asociacion = fields.Date(string="Fecha asociacion")
    fecha_vencimiento = fields.Date(string="Fecha afiliacion")
    plan = fields.Char(string="Plan")
    propietario = fields.Many2one('farmacia.paciente', string="Propietario")
    institucion_respaldadora = fields.Many2one('farmacia.institucion', 'Institucion')
    
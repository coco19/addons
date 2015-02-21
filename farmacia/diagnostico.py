# -*- coding: utf-8 -*-

from openerp import fields, models

class Diagnostico(models.Model):
    
    _name = 'farmacia.diagnostico'
    
    name = fields.Char(string = "Codigo")
    descripcion = fields.Text(string = "Descripcion")
    codifica = fields.Many2one('farmacia.capitulo')
    comprende = fields.Many2many('farmacia.afeccion', 'farmacia_diagnostico_afeccion', 'diagnostico_id', 'afeccion_id', string="Afeciones comprendidas")
    
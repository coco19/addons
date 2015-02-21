# -*- coding: utf-8 -*-

from openerp import fields, models

class Enfermedad(models.Model):
    
    _name = 'farmacia.enfermedad'
    
    nombre = fields.Char(string="Nombre")
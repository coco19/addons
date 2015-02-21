# -*- coding: utf-8 -*-

from openerp import models, fields

class Institucion(models.Model):
    _name = 'farmacia.institucion'
    
    nombre = fields.Char(string="Nombre institucion")
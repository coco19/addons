# -*- coding: utf-8 -*-

from openerp import fields, models

class Monodroga(models.Model):
    
    _name = 'farmacia.monodroga'
    
    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion")
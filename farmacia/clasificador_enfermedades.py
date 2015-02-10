# -*- coding: utf-8 -*-

from openerp import models, fields

class ClasificadorEnfermedades(models.Model):
    _name = 'farmacia.clasificador_enfermedades'
    
    nombre = fields.Char(string="Nombre clasificador")
    descripcion = fields.Text(string="Descripción")
    organizado_en = fields.One2many('farmacia.capitulo', 'organiza_clasificador', string="Capitulos")
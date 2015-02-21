# -*- coding: utf-8 -*-

from openerp import models, fields

class ListadoMedicamentos(models.Model):
    _name = 'farmacia.listado_medicamentos'
    
    nombre = fields.Char(string="Nombre listado")
    descripcion = fields.Text(string="Descripcion")
    medicamentos = fields.One2many('farmacia.articulo_vademecum', 'listado_en')
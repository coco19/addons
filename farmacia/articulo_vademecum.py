# -*- coding: utf-8 -*-

from openerp import models, fields

class ArticuloVademecum(models.Model):
    _name = 'farmacia.articulo_vademecum'
    
    presentacion = fields.Char(string="Presentacion")
    descripcion = fields.Text(string="Descripcion medicamento")
    listado_en = fields.Many2one('farmacia.listado_medicamentos', string = "Listado")
    monodrogas = fields.Many2many('farmacia.monodroga', string="Monodrogas")
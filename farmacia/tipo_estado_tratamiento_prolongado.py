# -*- coding: utf-8 -*-

from openerp import fields, models

class TipoEstadoTratamientoProlongado(models.Model):
    _name = 'farmacia.tipo_estado_tratamiento_prolongado'
    
    nombre = fields.Char()
    descripcion = fields.Text()
    estados_historicos = fields.One2many('farmacia.tratamiento_prolongado_estado', 'tipo_estado')
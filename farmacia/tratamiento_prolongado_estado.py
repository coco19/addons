# -*- coding: utf-8 -*-

from openerp import fields, models

class TratamientoProlongadoEstado(models.Model):
    _name = 'farmacia.tratamiento_prolongado_estado'
    
    fecha_hora_cambio = fields.Datetime()
    observacion = fields.Text()
    tratamiento_prolongado = fields.Many2one('farmacia.tratamiento_prolongado')
    tipo_estado = fields.Many2one('farmacia.tipo_estado_tratamiento_prolongado')
    
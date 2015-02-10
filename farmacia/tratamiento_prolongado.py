# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError

class TratamientoProlongado(models.Model):
    _name = 'farmacia.tratamiento_prolongado'

    #numeroTP = fields.Integer(string = "Número tratamiento prolongado")
    numero_receta = fields.Integer(string = "Número de receta")
    observaciones = fields.Text(string = "Observaciones")
    fecha_creacion = fields.Date(default=fields.Date.today)
    fecha_vencimiento = fields.Date(string = "Fecha Vencimiento")
    indicaciones = fields.One2many('farmacia.tratamiento_prolongado_detalle','tratamiento_prolongado_id', string='indicaciones')
    prescripto_por = fields.Many2one('farmacia.medico', string="Medico prescriptor")
    pertenece_a = fields.Many2one('farmacia.paciente', string="Paciente")
    #diagnosticos = fields.Many2many('farmacia.diagnostico', string="Diagnosticos")
    
    #Definicion de los estados que puede tomar el tratamiento prolongado segun odoo
    
    state = fields.Selection([
        ('borrador',"Borrador"),
        ('activo', "Activo"),
        ('inactivoXM', "Inactivo por morosidad"),
        ('cancelado', "Cancelado"),
        ('finalizadaME',"Finalizada medicamentos expendidos"),
        ('finalizadaV', "Finalizada vencida")
    ],default='borrador')
    
    #restriccion python decorator
    
    @api.constrains('fecha_vencimiento')
    def _chequea_fecha_vencimiento(self):
        if self.fecha_vencimiento <= self.fecha_creacion:
            raise ValidationError("La fecha de vencimiento no puede ser menor o igual a la actual")
        
    # actualiza dias restantes para destacar los prontos a vencer (detalle para probar que se puede interactuar con la vista mostrando colores)
    # La vista de arbol puede setear atributos suplementarios para customizar su comportamiento
    #def _actualizar_dias_restantes(self):
    #    dias_restantes=     
    
    @api.one
    def accion_borrador(self):
        self.state = 'borrador'
    
    @api.one
    def accion_cancelar(self):
        self.state = 'cancelado'
    
    @api.one
    def accion_activar(self):
        self.state = 'activo'

    # sobreescribo la funcionalidad del create que es el que crea el registro en la base de datos y esta relacionado
    # con el boton create-save-guardar
        
    def write(cr, uid, ids, vals, context=None):
        vals['state']='activo'
        super(your_class_name, self).write(cr, uid, ids, vals, context=context)
    
    
class TratamientoProlongadoDetalle(models.Model):
    _name = 'farmacia.tratamiento_prolongado_detalle'
    
    dosificacion = fields.Integer(string = "Dosificación en horas")
    dias_de_tratamiento = fields.Float(string = "Días de tratamiento", digits = (3, 0))
    
    tratamiento_prolongado_id = fields.Many2one('farmacia.tratamiento_prolongado', ondelete='cascade', string="Tratamiento prolongado")
    
     
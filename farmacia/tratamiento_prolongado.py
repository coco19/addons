# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import datetime
import xml.etree.ElementTree as ET

class TratamientoProlongado(models.Model):
    _name = 'farmacia.tratamiento_prolongado'
    _rec_name = 'id'

    #numeroTP = fields.Integer(string = "Número tratamiento prolongado")
    numero_receta = fields.Integer(string = "Número de receta")
    observaciones = fields.Text(string = "Observaciones")
    fecha_creacion = fields.Date(default=fields.Date.today)
    fecha_vencimiento = fields.Date(string = "Fecha Vencimiento")
    indicaciones = fields.One2many('farmacia.tratamiento_prolongado_detalle','tratamiento_prolongado_id', string='indicaciones')
    prescripto_por = fields.Many2one('farmacia.medico', string="Medico prescriptor")
    pertenece_a = fields.Many2one('farmacia.paciente', string="Paciente")
    diagnosticos = fields.Many2many('farmacia.diagnostico', 'farmacia_tratamiento_prolongado_diagnostico', 'tratamiento_prolongado_id', 'diagnostico_id', string="Diagnosticos")
    estados = fields.One2many('farmacia.tratamiento_prolongado_estado', 'tratamiento_prolongado')
    #relacion con la afiliacion
    numero_afiliado = fields.Many2one('farmacia.afiliacion', string="Numero afiliado")
    #falta traer los datos del paciente para mostrar en la cabecera
    #paciente_dni = fields.function(get_dni_paciente, type='int', string="DNI")
    #paciente_dni = fields.Integer(string="DNI", related='pertenece_a.nombre')
    paciente_dni = fields.Integer(string="DNI", related='pertenece_a.dni')
    paciente_telefono = fields.Integer(string="Telefono", related='pertenece_a.telefono')
    paciente_fecha_nacimiento = fields.Date(string="Fecha nacimiento", related='pertenece_a.fecha_nacimiento')
    paciente_domicilio = fields.Char(string="Domicilio", related='pertenece_a.domicilio')
    afiliado_plan = fields.Char(string="Plan", related='numero_afiliado.plan')
    #plan = numero_afiliado.institucion_respaldadora.nombre - esto estaria mal, no es un atributo que voy a asignar
    #a partir de seleccionar las monodrogas deberia seleccionar entre las presentaciones que tienen esa monodroga
    #presentacion = 
    
    
    #Definicion de los estados que puede tomar el tratamiento prolongado segun odoo
    
    state = fields.Selection([
        ('borrador',"Borrador"),
        ('activo', "Activo"),        
        ('finalizadaME',"Expendido"),
        ('vencido', "Vencido"),
        ('cancelado', "Cancelado"),
    ])
    
    #,default='borrador'
    
    #restriccion python decorator
    
    def get_fecha_actual(self):
        return str(datetime.now())
    
    #def get_dni_paciente(self):
    #    if self.pertenece_a:
    #        return pertenece_a.dni
    
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
        self.set_estado('cancelado', ' ')
        self.state = 'cancelado'
        return
    
    @api.one
    def accion_activar(self):        
        self.set_estado('activo', ' ')
        self.state = 'activo'
        return
    
    @api.one
    def verificar_vencimiento(self):
        # 2015-02-14
        #if (self.fecha_vencimiento <= fields.Date.today()):
        self.set_estado('vencido', ' ')
        self.state = 'vencido'        
        return
        
    # setea el estado del tratamiento prolongado
    def set_estado(self, nombre_tipo_estado, observacion):
        # setea el entorno
        #env_tipo_estado = (cr, uid, context)
        # busca la clase tipo estado del tatamiento prolongado adecuada
        
        tipo_estado_clase = self.env['farmacia.tipo_estado_tratamiento_prolongado']
        
        #tipo_estado_clase = self.pool.get('farmacia.tipo_estado_tratamiento_prolongado')
        
        # busco el tipo estado que me interesa
        #tipo_estado_objeto = tipo_estado_clase.search(['nombre', '=', nombre_tipo_estado])
        tipo_estado_objeto = tipo_estado_clase.search([['nombre', '=', nombre_tipo_estado]])
        # crea el estado historico, setea sus atributos simples y relacionales
        
        estado_historico_clase = self.env['farmacia.tratamiento_prolongado_estado']
        
        
        estado_historico_clase.create({'fecha_hora_cambio':datetime.now(),
            'observacion':observacion, 'tipo_estado':tipo_estado_objeto.id, 'tratamiento_prolongado':self.id  
        }) 
        #estado_historial = tipo_estado_clase.create()
        #estado_historial.fecha_hora_cambio = Datetime.now()
        #estado_historial.observacion = observacion
        #estado_historial.tipo_estado = tipo_estado_objeto.id
        #estado_historial.tratamiento_prolongado = self.id
        
        return
        

    # sobreescribo la funcionalidad del create que es el que crea el registro en la base de datos y esta relacionado
    # con el boton create-save-guardar
        
    #def write(cr, uid, ids, vals, context=None):
    #    vals['state']='activo'
    #    super(your_class_name, self).write(cr, uid, ids, vals, context=context)
    
    def fields_view_get(self, cr, uid, view_id=None, view_type=False, context=None, toolbar=False, submenu=False): 
        res = super(TratamientoProlongado,self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
        doc = ET.XML(res['arch'])
        print doc
        """
            if state == 'activo' :
                elemento=doc.xpath("/html/body/div[1]/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td[1]/div/div[2]/span[1]/div/button")
            elif state == 'B':
                view_id = self.pool.get('ir.ui.view').search(cr,uid,[('name', '=', 'child.form')])
        res = super(my_module,self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
        """
        return res
    
class TratamientoProlongadoDetalle(models.Model):
    _name = 'farmacia.tratamiento_prolongado_detalle'
    
    dosificacion = fields.Integer(string = "Dosificación en horas")
    dias_de_tratamiento = fields.Float(string = "Días de tratamiento", digits = (3, 0))
    
    tratamiento_prolongado_id = fields.Many2one('farmacia.tratamiento_prolongado', ondelete='cascade', string="Tratamiento prolongado")
    monodroga = fields.Many2one('farmacia.monodroga', string="Monodroga")
    
     
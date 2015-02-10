# -*- coding: utf-8 -*-

from openerp import fields, models, api

class Paciente (models.Model):
    
    _inherits = {
        'res.partner' : 'partner_id'
    }
    
    _name = 'farmacia.paciente'
    
    dni = fields.Integer(string = "DNI")
    nombre = fields.Char(string = "Nombre", required=True)
    apellido = fields.Char(string = "Apellido", required=True)
    fecha_nacimiento = fields.Date(string = "Fecha nacimiento")
    domicilio = fields.Char(string = "Domicilio")
    telefono = fields.Integer(string = "Teléfono")
    numero_socio = fields.Integer(string = "Número Socio")
    
    @api.onchange('nombre', 'apellido')
    def _onchange_nombre_apellido(self):
        self.name = str(self.nombre) + " " + str(self.apellido)
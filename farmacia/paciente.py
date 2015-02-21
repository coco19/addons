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
    afiliaciones = fields.One2many('farmacia.afiliacion', 'propietario',string = "Número Socio")
    
    @api.onchange('nombre', 'apellido')
    def _onchange_nombre_apellido(self):
        self.name = str(self.nombre) + " " + str(self.apellido)
    
    """
    def name_search(self,name='',args=None, operator='ilike', limit=100):
        if not args:    
            args = []
        if name:
            ids = self.search([('name',self.operator,self.name)]+ args, limit=limit)
        else:
            ids = self.search(args, limit=limit)
        result = self.name_get(ids)
        return result
    """
    
    #filtro para que cuando el usuario empiece a cargar el nombre o dni del paciente le busque el paciente
    #que esta en los registros
    
    def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if name:
            ids = self.search(cr, user, ['|',('name',operator,name),('dni',operator,name)]+ args, limit=limit, context=context)
        else:
            ids = self.search(cr, user, args, limit=limit, context=context)
        result = self.name_get(cr, user, ids, context=context)
        return result
    
from odoo import models, fields, api



class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    custom_payment_method  = fields.Char(string='P M')

    
    

class HospitalPatient(models.Model):
    _name = 'custom.module'
    _description = 'created for custom module'

    name = fields.Char(string='Name', required= True)
    age = fields.Integer('Age')
    payment_method = fields.Text('Payment Method')
    
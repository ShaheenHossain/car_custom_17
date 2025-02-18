
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'


    car_brand = fields.Char(string="Brand")
    vehicle_id = fields.Many2one('fleet.vehicle', string="Brand")
    chassis_no = fields.Char(string="Chassis No.")
    registration_plate = fields.Char(string="Registration Plate")

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    car_brand = fields.Char(string="Brand", related="partner_id.car_brand", store=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string="Brand")
    chassis_no = fields.Char(string="Chassis No.", related="partner_id.chassis_no", store=True)
    registration_plate = fields.Char(string="Registration Plate", related="partner_id.registration_plate", store=True)

class AccountMove(models.Model):
    _inherit = 'account.move'

    car_brand = fields.Char(string="Brand", related="partner_id.car_brand", store=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string="Brand")
    chassis_no = fields.Char(string="Chassis No.", related="partner_id.chassis_no", store=True)
    registration_plate = fields.Char(string="Registration Plate", related="partner_id.registration_plate", store=True)

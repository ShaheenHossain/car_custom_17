#
# from odoo import models, fields
#
# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#
#
#     car_brand = fields.Char(string="Brand")
#     vehicle_id = fields.Many2one('fleet.vehicle', string="Brand")
#     chassis_no = fields.Char(string="Chassis No.")
#     registration_plate = fields.Char(string="Registration Plate")
#     schadennr = fields.Char(string="SchadenNr.:")
#
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     car_brand = fields.Char(string="Brand", related="partner_id.car_brand", store=True)
#     vehicle_id = fields.Many2one('fleet.vehicle', string="Brand")
#     chassis_no = fields.Char(string="Chassis No.", related="partner_id.chassis_no", store=True)
#     registration_plate = fields.Char(string="Registration Plate", related="partner_id.registration_plate", store=True)
#     schadennr = fields.Char(string="SchadenNr.:")
#
#
# class AccountMove(models.Model):
#     _inherit = 'account.move'
#
#     car_brand = fields.Char(string="Brand", related="partner_id.car_brand", store=True)
#     vehicle_id = fields.Many2one('fleet.vehicle', string="Brand")
#     chassis_no = fields.Char(string="Chassis No.", related="partner_id.chassis_no", store=True)
#     registration_plate = fields.Char(string="Registration Plate", related="partner_id.registration_plate", store=True)
#     schadennr = fields.Char(string="SchadenNr.:")





from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle/Brand")  # Select the vehicle in contacts
    chassis_no = fields.Char(string="Chassis No.")
    # registration_plate = fields.Char(string="Registration Plate")
    schadennr = fields.Char(string="SchadenNr.:")


    registration_plate = fields.Char(
        related="vehicle_id.license_plate",
        string="Registration Plate",
        store=True
    )

    # chassis_no = fields.Char(string="Chassis No.", related="vehicle_id.chassis_no", store=True)

    # registration_plate = fields.Char(string="Registration Plate")

    @api.onchange('chassis_no')
    def _onchange_chassis_no(self):
        if self.chassis_no:
            vehicle = self.env['fleet.vehicle'].search(
                [('vin_sn', '=', self.chassis_no)],
                limit=1
            )
            if vehicle:
                self.vehicle_id = vehicle.id

    @api.onchange('registration_plate')
    def _onchange_registration_plate(self):
        if self.registration_plate:
            vehicle = self.env['fleet.vehicle'].search(
                [('license_plate', '=', self.registration_plate)],
                limit=1
            )
            if vehicle:
                self.vehicle_id = vehicle.id



    @api.onchange('vehicle_id')
    def _onchange_vehicle_id(self):
        if self.vehicle_id:
            self.chassis_no = self.vehicle_id.vin_sn





class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle/Brand", related="partner_id.vehicle_id", store=True)
    chassis_no = fields.Char(string="Chassis No.", related="partner_id.chassis_no", store=True)
    registration_plate = fields.Char(string="Registration Plate", related="partner_id.registration_plate", store=True)
    schadennr = fields.Char(string="SchadenNr.:")


class AccountMove(models.Model):
    _inherit = 'account.move'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle/Brand", related="partner_id.vehicle_id", store=True)
    chassis_no = fields.Char(string="Chassis No.", related="partner_id.chassis_no", store=True)
    registration_plate = fields.Char(string="Registration Plate", related="partner_id.registration_plate", store=True)
    schadennr = fields.Char(string="SchadenNr.:")


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle")
    chassis_no = fields.Char(string="Chassis No.")
    registration_plate = fields.Char(string="Registration Plate")

    schadennr = fields.Char(string="SchadenNr.:")


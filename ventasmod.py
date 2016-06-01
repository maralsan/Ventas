from openerp.osv import osv, fields
class pedido_venta(osv.Model):
 _inherit = 'sale.order'
 _columns = {
 'x_fecha': fields.date('Fecha', required='True'),
 'x_urgente': fields.boolean('Pedido Urgente'),
 }
{
    'name': 'Car Custom swiss',
    'version': '17.0.0.0.1',
    'depends': ['base', 'mail', 'account', 'sale', 'web'],
    'data': [
        'views/sale_order.xml',
        # 'security/ir.model.access.csv',

    ],

    'assets': {
        'web.assets_backend': [
            # 'web/static/src/js/widgets/form_controller.js',  # Path to FormController
            # 'web/static/src/js/core/rpc.js',  # Path to rpc
            # 'etohobil/static/src/js/sync_amount.js',
        ]
    },

    'application': True,
}

{
    'name': 'Warranty',
    'version': '16.0.1.0.0',
    'category': 'Warranty',
    'sequence': 1,
    'summary': 'product warranty',
    'description': "This is most popular Product Warranty Application",
    'website': 'https://www.odoo.com/page/productwarranty',
    'depends': [
        'base', 'account', 'stock', 'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_view.xml',
        'views/view.xml'

     ],
    'installable': True,
    'application': True
}
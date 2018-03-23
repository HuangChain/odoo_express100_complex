# -*- coding: utf-8 -*-
{
    'name': "kuaidi",

    'summary': """
        使用快递100作为平台，查询常用快递公司的物流信息""",

    'description': """
        此模块依赖于库存模块，继承自库存模块的分拣model，需要进入库存-作业-所有调拨-创建-额外的信息 方可看到效果！
    """,

    'author': "luomao",
    'website': "https://cdn.openerp.hk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': '辅助工具',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/kuaidi.xml',
    ],
    # only loaded in demonstration mode
}
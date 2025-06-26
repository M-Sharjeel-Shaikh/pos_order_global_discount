{
    "name": "POS - Global Discount & All Discount Display",
    "version": "16.0",
    "category": "Point of Sale",
    "summary": "Enable global discount functionality in POS and display "
               "all applied discounts for enhanced clarity and transparency.",
    "description": """ 
        This Odoo module enhances the Point of Sale (POS) experience by introducing a global discount feature and a 
        clear overview of all applied discounts. 

        Key Features:
        - Apply a global discount across the entire POS order with a single input.
        - Automatically exclude discount lines from total calculations to avoid misrepresentation.
        - Clearly display all applied discounts on the POS screen, improving cashier visibility and 
        customer communication.
        - Seamlessly integrates with Odoo’s native POS workflow without disrupting existing features.
        - Supports discount products and ensures accurate reporting for promotional tracking.
        
        Ideal for retail environments where bulk discounts or promotional offers are frequent, 
        this module simplifies discount handling while maintaining accuracy in sales data.
    """,

    "author": "Hi Spark Solutions",
    "company": "Hi Spark Solutions",
    "maintainer": "Hi Spark Solutions",
    "website": "https://www.hisparksolutions.com/",

    "depends": ["point_of_sale"],
    "demo": [
        "demo/product_product.xml",
        "demo/res_groups.xml",
    ],
    "data": [
        "views/view_product_template.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_order_global_discount/static/src/js/models.js",
            "pos_order_global_discount/static/src/xml/OrderSummary.xml",
        ],
        "web.assets_tests": [
            "pos_order_global_discount/tests/tours/PosDiscountAllTour.tour.js",
        ],
    },

    "images": ["static/description/banner.gif"],
    "qweb": [],
    "live_test_url": "",

    "license": "OPL-1",
    "application": True,
    "auto_install": False,
    "installable": True,
    "price": "5",
    "currency": "USD",
}

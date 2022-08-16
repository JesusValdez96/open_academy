{
    "name": "Open Academy",

    "summary": "Creation of the open academy module.",

    "author": "Jesús Valdez, Vauxoo",
    "website": "https://github.com/JesusValdez96/open_academy",

    "license": "LGPL-3",

    "category": "Customizations",
    "version": "15.0.1.0.0",

    "depends": [
        "base",
        "board",
    ],

    "data": [
        "security/res_groups.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "views/course_views.xml",
        "views/session_dashboard.xml",
        "views/session_views.xml",
        "views/res_partner_views.xml",
        "wizards/add_attendee_sessions_views.xml",
        "report/session_report.xml",
    ],

    "demo": [
        "demo/course_demo.xml",
    ],
}

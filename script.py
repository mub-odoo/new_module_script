import os

def create_module_structure(module_name, module_version):
    module_dir = module_name.lower().replace(' ', '_')

    init_content = '''# -*- coding: utf-8 -*
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# from . import 
'''
    
    # Create module directory
    os.makedirs(module_dir)

    # Create __init__.py file
    with open(os.path.join(module_dir, '__init__.py'), 'w') as main_init:
        main_init.write(init_content)
        # pass

    # Create models directory
    models_dir = os.path.join(module_dir, 'models')
    os.makedirs(models_dir)
    with open(os.path.join(models_dir, '__init__.py'), 'w') as init_file:
        init_file.write(init_content)
        # pass

    # Create views directory
    views_dir = os.path.join(module_dir, 'views')
    os.makedirs(views_dir)
    # with open(os.path.join(views_dir, '__init__.py'), 'w'):
    #     pass

    # Create security directory
    security_dir = os.path.join(module_dir, 'security')
    os.makedirs(security_dir)
    with open(os.path.join(security_dir, 'ir.model.access.csv'), 'w'):
        pass

    # Create data directory
    data_dir = os.path.join(module_dir, 'data')
    os.makedirs(data_dir)

    # Create static directory
    static_dir = os.path.join(module_dir, 'static')
    os.makedirs(static_dir)

    # Create manifest file
    manifest_content = '''# -*- coding: utf-8 -*
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "%s",
    "version": "%s",
    "summary": "module_summary",
    "description": """
       TASK ID - 
    """,
    "category": 'Customization',

    # Author
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "license": "LGPL-3",
    
    # Dependency
    "depends": [],
    
    "data": [
        # "security/ir.model.access.csv",
        # "views/view_file.xml",
    ],

    "installable": True,
    "application": False,
    "auto_install": False
}
''' % (module_name, module_version)
    with open(os.path.join(module_dir, '__manifest__.py'), 'w') as manifest_file:
        manifest_file.write(manifest_content)

if __name__ == '__main__':
    module_name = input('Enter the Module Technical Name: ')
    module_version = input('Enter the Module Version: ')
    create_module_structure(module_name, module_version)
    print('Module structure created successfully.')

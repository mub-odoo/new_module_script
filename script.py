# -*- coding: utf-8 -*
# Part of 4Minds. See LICENSE file for full copyright and licensing details.

import os
import content


def create_module_structure(module_name, module_version, file_contents):
    module_dir = module_name.lower().replace(' ', '_')
    
    # Create module directory
    os.makedirs(module_dir)

    # Create __init__.py file
    with open(os.path.join(module_dir, '__init__.py'), 'w') as main_init:
        main_init.write(file_contents.get('init_content'))

    # Create .gitignore file
    with open(os.path.join(module_dir, '.gitignore'), 'w') as GitIgnore:
        GitIgnore.write(file_contents.get('gitignore_content'))

    # Create models directory
    models_dir = os.path.join(module_dir, 'models')
    os.makedirs(models_dir)
    with open(os.path.join(models_dir, '__init__.py'), 'w') as init_file:
        init_file.write(file_contents.get('init_content'))
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
    manifest_content = file_contents.get('manifest_content') % (module_name, module_version)

    with open(os.path.join(module_dir, '__manifest__.py'), 'w') as manifest_file:
        manifest_file.write(manifest_content)

if __name__ == '__main__':
    module_name = input('Enter the Module Technical Name: ')
    module_version = input('Enter the Module Version: ')

    file_contents = {
        'init_content': content.init_content,
        'manifest_content': content.manifest_content,
        'gitignore_content': content.gitignore_content,
    }

    create_module_structure(module_name, module_version, file_contents)
    print('\nModule structure created successfully.')

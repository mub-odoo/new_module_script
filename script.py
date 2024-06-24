# -*- coding: utf-8 -*
# Part of 4Minds. See LICENSE file for full copyright and licensing details.

import os
import content


def create_module_structure(module_name, module_version, file_contents):
    ModuleDir = module_name.lower().replace(' ', '_')
    
    # Create module directory
    os.makedirs(ModuleDir)

    # Create __init__.py file
    with open(os.path.join(ModuleDir, '__init__.py'), 'w') as MainInit:
        MainInit.write(file_contents.get('init_content'))

    # Create .gitignore file
    with open(os.path.join(ModuleDir, '.gitignore'), 'w') as GitIgnore:
        GitIgnore.write(file_contents.get('gitignore_content'))

    # Create models directory
    ModelsDir = os.path.join(ModuleDir, 'models')
    os.makedirs(ModelsDir)
    with open(os.path.join(ModelsDir, '__init__.py'), 'w') as init_file:
        init_file.write(file_contents.get('init_content'))
        # pass

    # Create views directory
    ViewsDir = os.path.join(ModuleDir, 'views')
    os.makedirs(ViewsDir)
    # with open(os.path.join(ViewsDir, '__init__.py'), 'w'):
    #     pass

    # Create security directory
    SecurityDir = os.path.join(ModuleDir, 'security')
    os.makedirs(SecurityDir)
    with open(os.path.join(SecurityDir, 'ir.model.access.csv'), 'w'):
        pass

    # Create data directory
    DataDir = os.path.join(ModuleDir, 'data')
    os.makedirs(DataDir)

    # Create static directory
    StaticDir = os.path.join(ModuleDir, 'static')
    os.makedirs(StaticDir)

    # Create manifest file
    ManifestContent = file_contents.get('manifest_content') % (module_name, module_version)

    with open(os.path.join(ModuleDir, '__manifest__.py'), 'w') as manifest_file:
        manifest_file.write(ManifestContent)

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

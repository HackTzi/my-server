import os
import yaml
from PyInquirer import prompt


def read_proyects(file_path):
    with open(file_path) as file:
        projects_list = yaml.load(file, Loader=yaml.FullLoader)

        return projects_list


def deploy_project(project):
    deploy_command = project.get('deploy-command', None)
    if deploy_command is not None:
        print('Deploy proyect...')
        os.system(f'{deploy_command} &')
    else:
        print('[!] Please ensure provide the deploy_command in your proyects.yml')


def options_manager():
    projects = read_proyects('../projects.yaml')
    options = [{
        'type': 'list',
        'name': 'project_list',
        'message': 'Choose a project that you want to deploy.',
        'choices': ['All', *projects.keys()]
    }]

    project_to_deploy = prompt(options)

    if project_to_deploy['project_list'] == 'All':
        for project_name, values in projects.items():
            print(project_name)
            deploy_project(values)
    else:
        project = project_to_deploy['project_list']
        print(project)
        deploy_project(projects[project])


if __name__ == '__main__':
    print("""
       _____                              __  ___                                 
      / ___/___  ______   _____  _____   /  |/  /___ _____  ____ _____ ____  _____
      \__ \/ _ \/ ___/ | / / _ \/ ___/  / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
     ___/ /  __/ /   | |/ /  __/ /     / /  / / /_/ / / / / /_/ / /_/ /  __/ /    
    /____/\___/_/    |___/\___/_/     /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                                         /____/             
    """)
    options_manager()

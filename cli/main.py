import os
import re
import yaml


def read_proyects(file_path):
    with open(file_path) as file:
        projects_list = yaml.load(file, Loader=yaml.FullLoader)

        return projects_list


def update_and_deploy_project(project):
    repository = project.get('repository', None)
    if repository is not None:
        project_name = project['name']
        project_path = os.path.exists(f'~/server/{project_name}/')
        project_git = os.path.exists(f'~/server/{project_name}/.git/')

        if project_path and project_git:
            project_branch = project['deploy-branch']
            os.system(f'git pull origin {project_branch}')
        else:
            project_repository = project['repository']
            regex = """^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"""
            if re.match(regex, project_repository):
                os.system(f'git clone {project_repository}')
            else:
                print('[!] Please ensure that the repository is an url.')
               
        deploy_command = project.get('deploy-command', None)
        
        if deploy_command is not None:
            print('Deploy proyect...')
            os.system(f'cd {project_path} && {deploy_command} &')
        else:
            print('[!] Please ensure provide the deploy_command in your projects.yml')

    else:
        print('[!] Please ensure provide the repository in your projects.yml')


def main():
    projects = read_proyects('../projects.yaml')
    for project_name, values in projects.items():
        values['name'] = project_name
        update_and_deploy_project(project)

if __name__ == '__main__':
    print("""
       _____                              __  ___                                 
      / ___/___  ______   _____  _____   /  |/  /___ _____  ____ _____ ____  _____
      \__ \/ _ \/ ___/ | / / _ \/ ___/  / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
     ___/ /  __/ /   | |/ /  __/ /     / /  / / /_/ / / / / /_/ / /_/ /  __/ /    
    /____/\___/_/    |___/\___/_/     /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                                         /____/             
    """)
    main()

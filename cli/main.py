import os
import re
import yaml


def read_proyects(file_path):
    with open(file_path) as file:
        projects_list = yaml.load(file, Loader=yaml.FullLoader)

        return projects_list


def clone_or_update_project(project):
    repository = project.get('repository', None)
    if repository is not None:
        project_name = project['name']
        project_path = os.path.exists(f'~/server/{project_name}/')

        if project_path:
            project_branch = project['deploy-branch']
            os.system(f'git pull origin {project_branch}')
        else:
            project_repository = project['repository']
            regex = """^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"""
            if re.match(regex, project_repository):
                os.system(f'git clone {project_repository}')
            else:
                print('[!] Please ensure that the repository is an url.')
    else:
        print('[!] Please ensure provide the repository in your proyects.yml')


def deploy_project(project):
    deploy_command = project.get('deploy-command', None)
    if deploy_command is not None:
        print('Deploy proyect...')
        os.system(f'{deploy_command} &')
    else:
        print('[!] Please ensure provide the deploy_command in your proyects.yml')


def main():
    projects = read_proyects('../projects.yaml')
    for project_name, values in projects.items():
        print(project_name)
        values['name'] = project_name
<<<<<<< HEAD
        clone_or_update_project(values)
=======
        clone_or_update_proyect(values)
>>>>>>> b1c291719e1aecea91ea46a546469c3709e5db1f
        deploy_project(values)


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

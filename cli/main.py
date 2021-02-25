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
        print('--- ' * 10)
        print(project_name)

        os.chdir(os.path.expanduser('~'))

        if not os.path.isdir('server/'):
            os.mkdir('server/')

        os.chdir('server/')

        project_path = os.path.isdir(f'./{project_name}/')
        project_git = os.path.isdir(f'./{project_name}/.git/')

        if project_path and project_git:
            print('Update project...')
            project_branch = project.get('deploy-branch', None)

            if project_branch is not None:
                os.chdir(project_name)
                os.system(f'git pull origin {project_branch}')
            else:
                print('[!] Please ensure to provide deploy-branch.')

        else:
            print('Clone project...')
            project_repository = project.get('repository', None)

            if project_repository is not None:
                regex = """^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"""
                if re.match(regex, project_repository):
                    os.system(f'git clone {project_repository}')
                    os.chdir(project_name)
                else:
                    print('[!] Please ensure that the repository is an url.')

        deploy_command = project.get('deploy-command', None)

        if deploy_command is not None:
            print('Deploy project...')
            os.system(f'{deploy_command} &')
        else:
            print('[!] Please ensure provide the deploy_command in your projects.yml')

    else:
        print('[!] Please ensure provide the repository in your projects.yml')


def main():
    projects = read_proyects('../projects.yaml')
    for project_name, values in projects.items():
        values['name'] = project_name
        update_and_deploy_project(values)


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

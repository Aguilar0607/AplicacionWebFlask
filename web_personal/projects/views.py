########## Imports Flask & Python ##########
from flask import  render_template, request, Blueprint

project_blueprint = Blueprint('project', __name__)

#### localhost:5000/projects/list ####
#### localhost:5000/project/34 ####
#### localhost:5000/project/new ####
#### localhost:5000/project/34/edit ####
#### localhost:5000/project/34/delete ####

########## TODO: List Projects ##########
@project_blueprint.route('/list')
def list():
    projects = [
        {
            'name': 'Primer proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/home-bg.jpg',
            'url': 'https://www.google.com',
        },
        {
            'name': 'Segundo proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'https://www.xataka.com',
        },
        {
            'name': 'Segundo proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'https://www.xataka.com',
        },
        {
            'name': 'Segundo proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'https://www.xataka.com',
        }
    ]
    return render_template('project/list.html', projects=projects)

########## TODO: Show Project ##########
@project_blueprint.route('/<project_id>')
def show(project_id=None):
    return render_template('project/show.html', project_id=project_id)
    
########## TODO: Create New Project ##########
@project_blueprint.route('/new')
def new():
    return render_template('project/new.html')

########## TODO: Update a Project ##########
@project_blueprint.route('/<project_id>/edit')
def edit(project_id):
    return "Edit Page"

########## TODO: Delete a Project #########
@project_blueprint.route('/<project_id>/delete')
def delete(project_id):
    return "Delete Page"
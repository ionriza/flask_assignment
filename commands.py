from flask import Blueprint
from yaml import safe_load

bp = Blueprint('data', __name__)
bp.cli.short_help = 'Show the commands for CV.'

with open('cv.yml') as f:
    yml_data = safe_load(f.read())


@bp.cli.command('personal')
def personal():
    """Show personal data including name, mail and other."""
    print("\n".join([f"{attr.title()} = {yml_data.get(attr)}" for attr in ('name', 'mail', 'phone', 'experience')]))


@bp.cli.command('work')
def experience():
    """Show work experience including company's name, position and more."""
    work_experience = yml_data.get('work', [])
    print("\u001b[1m" + f"I've worked on {len(work_experience)} projects")
    for exp in work_experience:
        print('-' * 64)
        print("\u001b[42m" + f"{exp.get('position')} at {exp.get('company')}" + "\u001b[0m")
        print(f"From {exp.get('from')} to {exp.get('to')}"
              if exp.get('to') != 'Present' else f"I've been working since {exp.get('from')}")
        print(f"My tasks includes:")
        print("\n".join(map(lambda t: '- ' + t, exp.get('tasks', []))))


@bp.cli.command('education')
def education():
    """Show information regarding the education"""
    education_list = yml_data.get('education', [])
    for ed in education_list:
        print('-' * 64)
        print(f"Studied from {ed['from']} to {ed['to']}," if ed['to'] != 'Present' else 'Studying,', ed['subject'])
        print(f"at {ed['name']}")
        print(f"In order to get a {ed['degree']}")

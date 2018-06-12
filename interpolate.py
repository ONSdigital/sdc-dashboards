from jinja2 import Environment, FileSystemLoader 
import yaml

metrics = yaml.load(open('metrics.yml'))

environment = Environment(loader = FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
template = environment.get_template('template.html')
print(template.render(metrics))

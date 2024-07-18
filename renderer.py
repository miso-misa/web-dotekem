from jinja2 import Template, Environment, FileSystemLoader

# load templates folder to environment (security measure)
env = Environment(loader=FileSystemLoader('jinja_templates'))

# load the `index.jinja` template
index_template = env.get_template('index.html')
output_from_parsed_template = index_template.render()

# write the parsed template
with open("index.html", "w") as chap_page:
    chap_page.write(output_from_parsed_template)
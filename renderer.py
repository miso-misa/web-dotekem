from jinja2 import Template, Environment, FileSystemLoader
import os

# load templates folder to environment (security measure)
jinja_template_folder = "templates"
env = Environment(loader=FileSystemLoader(jinja_template_folder))

# load the `index.jinja` template
for f in os.listdir(jinja_template_folder):
    if f.endswith(".jinja"):
        template = env.get_template(f)
        output_from_parsed_template = template.render()
        # write the parsed template
        with open(f.replace(".jinja", ".html"), "w") as chap_page:
            chap_page.write(output_from_parsed_template)

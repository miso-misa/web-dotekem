from jinja2 import Template, Environment, FileSystemLoader
import os

# load templates folder to environment (security measure)
jinja_template_folder = "templates"
env = Environment(loader=FileSystemLoader(jinja_template_folder))
nav_bar = {
    "cz" : {
        "index.html" : "Domů",
        "shiatsu.html" : "Shiatsu",
        "about-me.html" : "O mně",
        "contact.html" : "Kontakt",
    },
    "en" : {
        "en_index.html" : "Home",
        "en_shiatsu.html" : "Shiatsu",
        "en_about-me.html" : "About me",
        "en_contact.html" : "Contact",
    },
}

pages = {
    "cz" : ["index", "shiatsu", "about-me", "contact", "GDPR",],
    "en" : ["en_index", "en_shiatsu", "en_about-me", "en_contact", "en_GDPR",],
}

homepage = {
    "cz" : "index.html",
    "en" : "en_index.html",
}

gdpr = {
    "cz" : "GDPR.html",
    "en" : "en_GDPR.html",
}

def render_page(page, lang):
    template = env.get_template(page + ".jinja")
    if lang == "cz":
        other_page = "en_" + page
    else:
        other_page = page.replace("en_","")
    kwargs = {
        "nav_bar" : nav_bar[lang],
        "lang" : lang,
        "active_page" : page+".html",
        "homepage" : homepage[lang],
        "other_page" : other_page+".html",
        "gdpr" : gdpr[lang],
    }
    output_from_parsed_template = template.render(**kwargs)
    with open(page + ".html", "w") as chap_page:
        chap_page.write(output_from_parsed_template)
        print(page, end=", ")

for lang in ["cz", "en"]:
    for page in pages[lang]:
       render_page(page, lang) 
print()



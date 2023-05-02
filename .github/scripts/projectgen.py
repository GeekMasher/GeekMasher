
import os
import yaml
import argparse

parser = argparse.ArgumentParser("ProjectGenerator")
parser.add_argument("-p", "--project", default="./projects.yml")


arguments = parser.parse_args()

if not os.path.exists(arguments.project):
    print(f"Project file does not exist...")
    exit(1)

with open(arguments.project, 'r') as handle:
    projects = yaml.safe_load(handle)


OUTPUT = ""

for top_project in projects:
    title = top_project.get("title")
    OUTPUT += f"### {title}\n\n"

    OUTPUT += "| Project | Stars | Language(s) |\n"
    OUTPUT += "| :------ | :---: | :---------- |\n"

    for project in top_project.get("projects", []):
        name = project.get("name")
        repository = project.get("github", name)
        url = f"https://github.com/{repository}"
        note = project.get("note", "")
        description = project.get("description", note)

        badge = f"https://img.shields.io/github/stars/{repository}?style=flat-square"

        languages = ", ".join(project.get("languages", []))


        # OUTPUT += f"- [{name}]({url}) - ![{repository} badge]({badge})\n"
        OUTPUT += f"| [{name}]({url}) | ![]({badge}) | {languages} |\n"

    OUTPUT += "\n"

print(OUTPUT)



import os
import yaml
import argparse

parser = argparse.ArgumentParser("ProjectGenerator")
parser.add_argument("-p", "--project", default="./projects.yml")
parser.add_argument("-d", "--display-all", action="store_true")

arguments = parser.parse_args()

if not os.path.exists(arguments.project):
    print(f"Project file does not exist...")
    exit(1)

with open(arguments.project, 'r') as handle:
    projects = yaml.safe_load(handle)


OUTPUT = ""

for top_project in projects:
    title = top_project.get("title")

    if not arguments.display_all and top_project.get("hide", False):
        continue

    OUTPUT += f"### {title}\n\n"
    
    OUTPUT += "| Project (languages) | Stars / Activity |\n"
    OUTPUT += "| :------------------ | :--------------: |\n"

    for project in top_project.get("projects", []):
        name = project.get("name")
        if not arguments.display_all and project.get("hide", False):
            continue

        repository = project.get("github", name)
        url = f"https://github.com/{repository}"
        note = project.get("note", "")
        description = project.get("description", note)

        badge = f"https://img.shields.io/github/stars/{repository}?style=flat-square"
        activity = f"https://img.shields.io/github/last-commit/{repository}?style=flat-square"

        languages = ", ".join(project.get("languages", []))

        # OUTPUT += f"- [{name}]({url}) - ![{repository} badge]({badge})\n"
        OUTPUT += f"| [{name}]({url}) ({languages})| ![]({badge}) - ![activity]({activity}) |\n"

    OUTPUT += "\n"

print(OUTPUT)


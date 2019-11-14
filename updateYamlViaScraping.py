import yaml
from bs4 import BeautifulSoup as bs
import requests
import re
import itertools


def update_yaml(main_section, sub_section, wiki_extension):
    with open('confs/config.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/' + wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML")
    for i, li in enumerate(soup.select('li')):
        if list(li.attrs.keys()) == ['class']:
            pass
        elif list(li.attrs.keys()) == ['id']:
            pass
        elif list(li.attrs.keys()) == ['style']:
            pass
        else:
            x = li.text
            x = re.sub('[,.-]', '', x).replace('\'', '').replace(' (company)', '').replace(' (food company)', '').replace(' (chocolate)', '').replace(' (hot sauce)', '')
            data_loaded[main_section][sub_section].append(x)

    print("Removing Miscellaneous things added from Wikipedia")
    for item in data_loaded[main_section][sub_section]:
        if "List of " in item:
            data_loaded[main_section][sub_section].remove(item)

    print("Sorting and Dropping Duplicates")
    data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
    data_loaded[main_section][sub_section] = list(
        k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))

    print("Saving the Updated Yaml File")
    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Saved.")


update_yaml('case_agnostic_work', 'company_foodbev', 'List_of_food_companies')



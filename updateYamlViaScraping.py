import yaml
from bs4 import BeautifulSoup as bs
import requests
import re
import itertools


def update_yaml(main_section, sub_section, wiki_extension):
    with open('TESTING.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/' + wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML\n")
    for i, li in enumerate(soup.select('li')):
        if list(li.attrs.keys()) == ['class']:
            pass
        elif list(li.attrs.keys()) == ['id']:
            pass
        elif list(li.attrs.keys()) == ['style']:
            pass
        elif li.text == 'List of private equity firms':
            break
        elif li.text == 'Private equity firm':
            break
        elif li.text == 'List of bakeries':
            break
        elif li.text == 'List of largest biotechnology & pharmaceutical companies':
            break
        else:
            x = li.text
            x = x.split(' (')[0]
            x = re.sub('[,.-]', '', x).replace('\'', '').lstrip()
            print(x)
            data_loaded[main_section][sub_section].append(x)

    for item in data_loaded[main_section][sub_section]:
        if "List of " in item:
            data_loaded[main_section][sub_section].remove(item)

    print("\nSorting and Dropping Duplicates")
    data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
    data_loaded[main_section][sub_section] = list(
        k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table(main_section, sub_section,wiki_extension,col):
    with open('TESTING.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/'+wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML\n")

    try:
        right_table = soup.find('table', class_='sortable wikitable')
        for row in right_table.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) > 1:
                x = cells[col].text.split('[')[0].split(' /')[0].split('(')[0]
                x = re.sub('[,.-]', '', x).replace('\n', '').replace('\'', '').replace(' ^', '').lstrip()
                print(x)
                data_loaded[main_section][sub_section].append(x)
    except:
        try:
            right_table = soup.find('table', class_='wikitable sortable')
            for row in right_table.findAll('tr'):
                cells = row.findAll('td')
                if len(cells) > 1:
                    x = cells[col].text.split('[')[0].split(' /')[0].split('(')[0]
                    x = re.sub('[,.-]', '', x).replace('\n', '').replace('\'', '').replace(' ^', '').lstrip()
                    print(x)
                    data_loaded[main_section][sub_section].append(x)
        except:
            right_table = soup.find('table')
            for row in right_table.findAll('tr'):
                cells = row.findAll('td')
                if len(cells) > 1:
                    x = cells[col].text.split('[')[0].split(' /')[0].split('(')[0]
                    x = re.sub('[,.-]', '', x).replace('\n', '').replace('\'', '').replace(' ^', '').lstrip()
                    print(x)
                    data_loaded[main_section][sub_section].append(x)

    for item in data_loaded[main_section][sub_section]:
        if "List of " in item:
            data_loaded[main_section][sub_section].remove(item)

    print("\nSorting and Dropping Duplicates")
    data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
    data_loaded[main_section][sub_section] = list(k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table_index(main_section, sub_section, wiki_extension):
    with open('TESTING.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/' + wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML\n")

    try:
        right_table = soup.find('table', class_='sortable wikitable')
        for row in right_table.findAll('tr'):
            for col in row.findAll('th'):
                for tag in col.find_all(True):
                    if tag.text in ['Location', 'Partners', 'Industries', 'Assets under management']:
                        pass
                    else:
                        x = tag.text.split(" (")[0]
                        x = re.sub('[,.-]', '', x).replace('\n', '').replace('\'', '')
                        print(x)
                        data_loaded[main_section][sub_section].append(x)
    except:
        right_table = soup.find('table', class_='wikitable sortable')
        for row in right_table.findAll('tr'):
            for col in row.findAll('th'):
                for tag in col.find_all(True):
                    if tag.text in ['Location', 'Partners', 'Industries', 'Assets under management']:
                        pass
                    else:
                        x = tag.text.split(" (")[0]
                        x = re.sub('[,.-]', '', x).replace('\n', '').replace('\'', '')
                        print(x)
                        data_loaded[main_section][sub_section].append(x)

    for item in data_loaded[main_section][sub_section]:
        if "List of " in item:
            data_loaded[main_section][sub_section].remove(item)

    print("\nSorting and Dropping Duplicates")
    data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
    data_loaded[main_section][sub_section] = list(
        k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


# update_yaml('case_agnostic_work', 'company_foodbev', 'List_of_food_companies')
# update_yaml_table('case_agnostic_work', 'company_health', 'List_of_largest_biotechnology_and_pharmaceutical_companies', 1)
# update_yaml('case_agnostic_work',  'company_health', 'List_of_pharmaceutical_companies')
# update_yaml('case_agnostic_work', 'company_fin', 'List_of_asset_management_firms')
# update_yaml_table('case_agnostic_work', 'company_fin', 'List_of_asset_management_firms', 1)
# update_yaml('case_agnostic_work', 'company_fin', 'List_of_investment_banks')
# update_yaml_table_index('case_agnostic_work', 'company_fin', 'List_of_venture_capital_firms')
# update_yaml_table('case_agnostic_work', 'company_fin', 'List_of_private_equity_firms', 0)
# update_yaml_table('case_agnostic_work', 'company_fin', 'List_of_largest_banks', 1)
# update_yaml_table('case_agnostic_work', 'company_fin', 'List_of_systemically_important_banks', 0)
update_yaml_table('case_agnostic_work', 'company_consumer', 'List_of_swimwear_brands', 0)

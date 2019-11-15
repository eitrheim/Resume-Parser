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
        elif li.text == 'Fitness wear':
            break
        elif li.text == 'List of Canadian electric utilities':
            break
        elif li.text == 'List of energy storage projects':
            break
        elif li.text == 'List of investment banks':
            break
        elif li.text == 'List of largest biotechnology & pharmaceutical companies':
            break
        elif li.text == 'Lists of public utilities':
            break
        elif li.text == 'Canadian Petroleum Companies':
            break
        elif li.text == 'List of Illinois companies':
            break
        elif li.text == 'List of Danish wind turbine manufacturers':
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


def update_yaml_table1(main_section, sub_section, wiki_extension, col):
    with open('TESTING.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/'+wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML\n")

    right_table = soup.find('table', class_='sortable wikitable')
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
    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table2(main_section, sub_section, wiki_extension, col):
    with open('TESTING.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/'+wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML\n")

    right_table = soup.find('table', class_='wikitable sortable')
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
    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table3(main_section, sub_section, wiki_extension, col):
    with open('TESTING.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/'+wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML\n")

    right_table = soup.find('table', class_='wikitable plainrowheaders sortable')
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
    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table4(main_section, sub_section, wiki_extension, col):
    with open('TESTING.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/'+wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML\n")

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
    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table5(main_section, sub_section, wiki_extension):
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
# update_yaml_table1('case_agnostic_work', 'company_health', 'List_of_largest_biotechnology_and_pharmaceutical_companies', 1)
# update_yaml('case_agnostic_work',  'company_health', 'List_of_pharmaceutical_companies')
# update_yaml('case_agnostic_work', 'company_fin', 'List_of_asset_management_firms')
# update_yaml_table1('case_agnostic_work', 'company_fin', 'List_of_asset_management_firms', 1)
# update_yaml('case_agnostic_work', 'company_fin', 'List_of_investment_banks')
# update_yaml_table5('case_agnostic_work', 'company_fin', 'List_of_venture_capital_firms')
# update_yaml_table2('case_agnostic_work', 'company_fin', 'List_of_private_equity_firms', 0)
# update_yaml_table4('case_agnostic_work', 'company_fin', 'List_of_largest_banks', 1)
# update_yaml_table2('case_agnostic_work', 'company_fin', 'List_of_systemically_important_banks', 0)
# update_yaml_table2('case_agnostic_work', 'company_consumer', 'List_of_swimwear_brands', 0)
# update_yaml_table3('case_agnostic_work', 'company_consumer', 'List_of_sporting_goods_manufacturers', 0)
# update_yaml_table2('case_agnostic_work', 'company_consumer', 'List_of_lingerie_brands', 0)
# update_yaml('case_agnostic_work', 'company_consumer', 'List_of_fitness_wear_brands')
# update_yaml('case_agnostic_work', 'company_energychem', 'List_of_concentrating_solar_thermal_power_companies')
# update_yaml('case_agnostic_work', 'company_energychem', 'List_of_United_States_electric_companies')
# update_yaml('case_agnostic_work', 'company_energychem', 'List_of_United_States_water_companies')
# update_yaml('case_agnostic_work', 'company_energychem', 'List_of_oilfield_service_companies')
# update_yaml_table2('case_agnostic_work', 'company_energychem', 'List_of_largest_oil_and_gas_companies_by_revenue', 1)
# update_yaml_table2('case_agnostic_work', 'company_energychem', 'List_of_largest_chemical_producers', 1)
# update_yaml('case_agnostic_work', 'company_industrial', 'List_of_wind_turbine_manufacturers')
# update_yaml_table4('case_agnostic_work', 'company_industrial', 'List_of_traction_motor_manufacturers', 0)
# update_yaml('case_agnostic_work', 'company_services', 'List_of_management_consulting_firms')
# update_yaml('case_agnostic_work', 'company_industrial', 'List_of_touch-solution_manufacturers')
# update_yaml_table2('case_agnostic_work', 'company_energychem', 'List_of_steel_producers', 13)
# update_yaml_table4('case_agnostic_work', 'company_tech', 'Semiconductor_equipment_sales_leaders_by_year', 1)
# update_yaml_table2('case_agnostic_work', 'company_services', 'List_of_multiple-system_operators', 0)


update_yaml('case_agnostic_work', 'company_consumer', 'List_of_superstores')




# update_yaml('case_agnostic_work', 'company_other', 'List_of_companies_in_the_Chicago_metropolitan_area')
# update_yaml_table('case_agnostic_work', 'company_other', 'List_of_largest_companies_by_revenue', 0)
#delete dups in "other"

# https://en.wikipedia.org/wiki/List_of_United_States_natural_gas_companies
# https://en.wikipedia.org/wiki/List_of_oil_exploration_and_production_companies#North_America
# https://en.wikipedia.org/wiki/List_of_modern_armament_manufacturers
# https://en.wikipedia.org/wiki/List_of_automobile_manufacturers#U
# https://en.wikipedia.org/wiki/state_drive_manufacturers
# https://en.wikipedia.org/wiki/List_of_video_game_developers
# https://en.wikipedia.org/wiki/List_of_video_game_publishers
# https://en.wikipedia.org/wiki/List_of_United_States_over-the-air_television_networks
# https://en.wikipedia.org/wiki/List_of_United_States_pay_television_channels
# https://en.wikipedia.org/wiki/List_of_animation_studios





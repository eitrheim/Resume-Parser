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
        elif li.text == 'Private equity firm':
            break
        elif li.text == 'Fitness wear':
            break
        elif li.text == 'Canadian Petroleum Companies':
            break
        elif li.text == 'Casual':
            break
        elif li.text == 'Acorn Computers':
            break
        elif li.text == 'Enterprise search':
            break
        elif 'List of ' in li.text:
            break
        elif 'Lists of ' in li.text:
            break
        elif li.text == 'Electronic design':
            break
        elif li.text == 'Yazoo and Mississippi Valley Railroad':
            break
        elif li.text == 'Airline codes':
            break
        elif li.text == 'Telegram & Gazette':
            break
        elif li.text == 'Film treatment':
            break
        elif li.text == 'Ocean Freeze Frozen Yogurt':
            break
        elif li.text == 'Bass effects':
            break
        elif li.text == 'Multinational company topics':
            break
        else:
            x = li.text
            x = x.split(' (')[0].split('[')[0]
            x = re.sub('[,.-]', '', x).replace('\'', '').lstrip()
            print(x)
            data_loaded[main_section][sub_section].append(x)

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
    except IndexError:
        pass

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

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
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

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table2lists(main_section, sub_section, wiki_extension, col):
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
            for x in cells[col].text.split(','):
                x = x.split('[')[0].split(' /')[0].split('(')[0]
                x = re.sub('[.-]', '', x).replace('\n', '').replace('\'', '').replace(' ^', '').lstrip()
                if x != "":
                    print(x)
                    data_loaded[main_section][sub_section].append(x)

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
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

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
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

    right_table = soup.find('table', class_='wikitable')
    for row in right_table.findAll('tr'):
        cells = row.findAll('td')
        if len(cells) > 1:
            x = cells[col].text.split('[')[0].split(' /')[0].split('(')[0]
            x = re.sub('[,.-]', '', x).replace('\n', '').replace('\'', '').replace(' ^', '').lstrip()
            print(x)
            data_loaded[main_section][sub_section].append(x)

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table4all(main_section, sub_section, wiki_extension, col):
    with open('TESTING.yaml', 'r') as stream:
        try:
            data_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print("Accessing Wikipedia")
    html = requests.get('https://en.wikipedia.org/wiki/'+wiki_extension).text
    soup = bs(html, 'html.parser')
    print("Getting List Items and Adding to YAML\n")

    right_table = soup.findAll('table', class_='wikitable')
    for table in right_table:
        # print(table)
        for row in table.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) > 1:
                x = cells[col].text.split('[')[0].split(' /')[0].split('(')[0]
                x = re.sub('[,.-]', '', x).replace('\n', '').replace('\'', '').replace(' ^', '').lstrip()
                print(x)
                data_loaded[main_section][sub_section].append(x)

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table5(main_section, sub_section, wiki_extension, col):
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

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


def update_yaml_table6(main_section, sub_section, wiki_extension):
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

    try:
        data_loaded[main_section][sub_section] = sorted(data_loaded[main_section][sub_section], key=lambda x: x[0])
        data_loaded[main_section][sub_section] = list(
            k for k, _ in itertools.groupby(data_loaded[main_section][sub_section]))
        print("\nSorted and Dropped Duplicates")
    except IndexError:
        pass

    with open('TESTING.yaml', 'w') as fp:
        yaml.dump(data_loaded, fp)
    print("Updated Yaml File Saved")


update_yaml('case_agnostic_work', 'company_foodbev', 'List_of_food_companies')
# update_yaml_table1('case_agnostic_work', 'company_health', 'List_of_largest_biotechnology_and_pharmaceutical_companies', 1)
# update_yaml('case_agnostic_work', 'company_health', 'List_of_pharmaceutical_companies')
# update_yaml('case_agnostic_work', 'company_fin', 'List_of_asset_management_firms')
# update_yaml_table1('case_agnostic_work', 'company_fin', 'List_of_asset_management_firms', 1)
# update_yaml('case_agnostic_work', 'company_fin', 'List_of_investment_banks')
# update_yaml_table6('case_agnostic_work', 'company_fin', 'List_of_venture_capital_firms')
# update_yaml_table2('case_agnostic_work', 'company_fin', 'List_of_private_equity_firms', 0)
# update_yaml_table4('case_agnostic_work', 'company_fin', 'List_of_largest_banks', 1)
# update_yaml_table2('case_agnostic_work', 'company_fin', 'List_of_systemically_important_banks', 0)
# update_yaml_table2('case_agnostic_work', 'company_consumer', 'List_of_swimwear_brands', 0)
# update_yaml_table3('case_agnostic_work', 'company_consumer', 'List_of_sporting_goods_manufacturers', 0)
# update_yaml_table2('case_agnostic_work', 'company_consumer', 'List_of_lingerie_brands', 0)
# update_yaml('case_agnostic_work', 'company_consumer', 'List_of_fitness_wear_brands')
# update_yaml('case_agnostic_work', 'company_energychem', 'List_of_concentrating_solar_thermal_power_companies')
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
# update_yaml_table2('case_agnostic_work', 'company_consumer', 'List_of_supermarket_chains', 0)
# update_yaml('case_agnostic_work', 'company_consumer', 'List_of_pharmacies')
# update_yaml_table2('case_agnostic_work', 'company_consumer', 'List_of_chained-brand_hotels', 0)
# update_yaml_table2lists('case_agnostic_work', 'company_consumer', 'List_of_chained-brand_hotels', 6)
# update_yaml_table2lists('case_agnostic_work', 'company_consumer', 'List_of_chained-brand_hotels', 7)
# update_yaml_table2lists('case_agnostic_work', 'company_consumer', 'List_of_chained-brand_hotels', 8)
# update_yaml_table2lists('case_agnostic_work', 'company_consumer', 'List_of_chained-brand_hotels', 9)
# update_yaml_table2lists('case_agnostic_work', 'company_consumer', 'List_of_chained-brand_hotels', 10)
# update_yaml_table2lists('case_agnostic_work', 'company_consumer', 'List_of_chained-brand_hotels', 11)
# update_yaml_table2('case_agnostic_work', 'company_services', 'List_of_largest_law_firms_by_revenue', 1)
# update_yaml_table2('case_agnostic_work', 'company_services', 'List_of_largest_United_States-based_law_firms_by_head_count', 1)
# update_yaml('case_agnostic_work', 'company_services', 'List_of_marketing_research_firms')
# update_yaml('case_agnostic_work', 'company_consumer', 'List of executive search firms')
# update_yaml('case_agnostic_work', 'company_tech', 'List_of_computer_system_manufacturers')
# update_yaml('case_agnostic_work', 'company_tech', 'List_of_computer_hardware_manufacturers')
# update_yaml('case_agnostic_work', 'company_tech', 'List_of_advertising_technology_companies')
# update_yaml_table2('case_agnostic_work', 'company_tech', 'List_of_flash_memory_controller_manufacturers', 0)
# update_yaml_table4('case_agnostic_work', 'company_tech', 'List_of_EDA_companies', 0)
# update_yaml_table2('case_agnostic_work', 'company_tech', 'List_of_electric-vehicle-battery_manufacturers', 0)
# update_yaml_table2('case_agnostic_work', 'company_services', 'List_of_telephone_operating_companies', 1)
# update_yaml('case_agnostic_work', 'company_energychem', 'List_of_silicon_producers')
# update_yaml_table2('case_agnostic_work', 'company_tech', 'List_of_photovoltaics_companies', 0)
# update_yaml_table4all('case_agnostic_work', 'company_consumer', 'List_of_airlines_of_the_United_States', 0)
# update_yaml_table5('case_agnostic_work', 'company_consumer', 'List_of_casinos_in_the_United_States', 0)
# update_yaml_table2('case_agnostic_work', 'company_consumer', 'List_of_cruise_lines', 0)
# update_yaml('case_agnostic_work', 'company_industrial', 'List_of_Class_I_railroads')
# update_yaml('case_agnostic_work', 'company_consumer', 'List_of_charter_airlines')
# update_yaml_table2('case_agnostic_work', 'company_services', 'List_of_largest_container_shipping_companies', 0)
# update_yaml('case_agnostic_work', 'company_tech', 'List_of_system-on-a-chip_suppliers')
# update_yaml_table2('case_agnostic_work', 'company_tech', 'List_of_companies_involved_in_quantum_computing_or_communication', 0)
# update_yaml_table2('case_agnostic_work', 'company_tech', 'List_of_data_recovery_companies', 0)
# update_yaml_table4all('case_agnostic_work', 'company_services', 'List_of_IT_consulting_firms', 0)
# update_yaml_table4('case_agnostic_work', 'company_tech', 'List_of_largest_Internet_companies', 1)
# update_yaml_table4('case_agnostic_work', 'company_fin', 'List_of_hedge_funds', 1)
# update_yaml_table4('case_agnostic_work', 'company_services', 'List_of_newspapers_in_the_United_States', 1)
# update_yaml_table4('case_agnostic_work', 'company_services', 'List_of_newspapers_by_circulation', 0)
# update_yaml('case_agnostic_work', 'company_services', 'List_of_newspapers_serving_cities_over_100,000_in_the_United_States')
# update_yaml_table4all('case_agnostic_work', 'company_consumer', 'List_of_restaurant_chains_in_the_United_States', 0)
# update_yaml_table4all('case_agnostic_work', 'company_industrial', 'List_of_largest_manufacturing_companies_by_revenue', 1)
# update_yaml('case_agnostic_work', 'company_fin', 'List_of_United_States_insurance_companies')
# update_yaml('case_agnostic_work', 'company_fin', 'List_of_international_banking_institutions')
# update_yaml_table4all('case_agnostic_work', 'company_tech', 'Semiconductor_equipment_sales_leaders_by_year', 2)
# update_yaml_table4('case_agnostic_work', 'company_energychem', 'List_of_largest_aluminum_producers_by_output', 1)
# update_yaml('case_agnostic_work', 'company_other', 'List_of_companies_in_the_Chicago_metropolitan_area')
# update_yaml_table2('case_agnostic_work', 'company_other', 'List_of_largest_companies_by_revenue', 0)
# update_yaml_table4('case_agnostic_work', 'company_tech', 'List_of_glossy_display_branding_manufacturers', 0)
# update_yaml_table4('case_agnostic_work', 'company_consumer', 'List_of_bean-to-bar_chocolate_manufacturers', 0)
# update_yaml('case_agnostic_work', 'company_consumer', 'List_of_frozen_yogurt_companies')
# update_yaml('case_agnostic_work', 'company_services', 'List_of_websites_about_food_and_drink')
# update_yaml('case_agnostic_work', 'company_tech', 'List_of_bass_amplifier_and_loudspeaker_manufacturers')
# update_yaml_table4('case_agnostic_work', 'company_tech', 'List_of_digital_camera_brands', 2)
# update_yaml_table4all('case_agnostic_work', 'company_other', 'List_of_SRI_International_spin-offs', 0)
# update_yaml_table4('case_agnostic_work', 'company_other', 'List_of_largest_European_manufacturing_companies_by_revenue', 0)
# update_yaml('case_agnostic_work', 'company_other', 'List_of_Six_Sigma_companies')
# update_yaml_table4('case_agnostic_work', 'company_other', 'List_of_S%26P_500_companies', 1)
# update_yaml('case_agnostic_work', 'company_other', 'List_of_multinational_corporations')
# update_yaml_table4('case_agnostic_work', 'company_other', 'List_of_companies_of_the_European_Union', 1)
# update_yaml_table4('case_agnostic_work', 'company_energychem', 'List_of_copper_production_by_company', 1)
# update_yaml_table4all('case_agnostic_work', 'company_other', 'List_of_largest_corporate_profits_and_losses', 1)





# deleting companies in 'other' if they are in another section
with open('TESTING.yaml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)

for company_type in data_loaded['case_agnostic_work'].keys():
    if company_type == 'company_other':
        pass
    else:
        for item in data_loaded['case_agnostic_work'][company_type]:
            if item in data_loaded['case_agnostic_work']['company_other']:
                data_loaded['case_agnostic_work']['company_other'].remove(item)
                print(item, "deleted from company_other")

with open('TESTING.yaml', 'w') as fp:
    yaml.dump(data_loaded, fp)




##################################################
# revisit
# update_yaml('case_agnostic_work', 'company_tech', 'List_of_3D_printer_manufacturers')
# update_yaml('case_agnostic_work', 'company_tech', 'List_of_semiconductor_IP_core_vendors')
# update_yaml('case_agnostic_work', 'company_tech', 'List_of_enterprise_search_vendors')
# update_yaml('case_agnostic_work', 'company_energychem', 'List_of_United_States_electric_companies')
##################################################
# figure out how to scrape these
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
# https://en.wikipedia.org/wiki/List_of_convenience_stores
# https://en.wikipedia.org/wiki/List_of_retailers%27_cooperatives
# https://en.wikipedia.org/wiki/List_of_department_stores_by_country
# https://en.wikipedia.org/wiki/List_of_game_manufacturers
# https://en.wikipedia.org/wiki/List_of_supermarket_chains_in_North_America
# https://en.wikipedia.org/wiki/List_of_bookstore_chains
# https://en.wikipedia.org/wiki/List_of_book_sales_clubs
# https://en.wikipedia.org/wiki/List_of_superstores
# https://en.wikipedia.org/wiki/List_of_cleaning_companies
# https://en.wikipedia.org/wiki/List_of_press_release_agencies
# https://en.wikipedia.org/wiki/List_of_CAx_companies
# https://en.wikipedia.org/wiki/List_of_electronics_brands
# https://en.wikipedia.org/wiki/List_of_bus_operating_companies
# https://en.wikipedia.org/wiki/List_of_big_data_companies
# https://en.wikipedia.org/wiki/Tech_companies_in_the_New_York_metropolitan_area
# https://en.wikipedia.org/wiki/List_of_banks_(alphabetical)
# https://en.wikipedia.org/wiki/List_of_mobile_network_operators
# https://en.wikipedia.org/wiki/List_of_communication_satellite_companies
# https://en.wikipedia.org/wiki/List_of_largest_biomedical_companies_by_revenue
# https://en.wikipedia.org/wiki/List_of_film_distributors_by_country#United_States
# https://en.wikipedia.org/wiki/List_of_solid-state_drive_manufacturers
# https://en.wikipedia.org/wiki/List_of_soft_drink_producers
# https://en.wikipedia.org/wiki/List_of_PLC_manufacturers
# https://en.wikipedia.org/wiki/List_of_major_arms_industry_corporations_by_country
# https://en.wikipedia.org/wiki/List_of_public_corporations_by_market_capitalization
# https://en.wikipedia.org/wiki/List_of_television_manufacturers
# https://en.wikipedia.org/wiki/List_of_flat_panel_display_manufacturers
# https://en.wikipedia.org/wiki/List_of_loudspeaker_manufacturers
# https://en.wikipedia.org/wiki/List_of_unicorn_startup_companies
# https://en.wikipedia.org/wiki/List_of_government-owned_companies
# https://en.wikipedia.org/wiki/List_of_holding_companies
# https://en.wikipedia.org/wiki/List_of_franchises
# https://en.wikipedia.org/wiki/List_of_largest_employers
# https://en.wikipedia.org/wiki/List_of_conglomerates
# https://en.wikipedia.org/wiki/List_of_company_registers#United_States




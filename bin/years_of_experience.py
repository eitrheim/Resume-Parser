import re

months = ['january','jan','february','feb','march','mar','april','apr','may','june','jun','july','jul',
          'august','aug','september','sept','sep','october','oct','november', 'nov', 'december', 'dec']

list_of_dates = []


def years_of_experience(input_string):
    input_string = input_string.lower().replace(')', ' - ').replace('–', ' - ').replace('-', ' - ').replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').replace('\'', ' ').replace('’', ' ')
    input_string = re.sub('[ ]+'," ", input_string)

    tokens = filter(None, re.split(r'(\S+|\W+)', input_string))
    tokens = list(tokens)
    for i in range(len(tokens)):
        if tokens[i] in months:
            try:
                if int(tokens[i+2]) in range(1970,2025):
                    if tokens[i+3] == ' - ':
                        if tokens[i+4] in ['current', 'present', 'today']:
                            list_of_dates.append(''.join(tokens[i:i+5]))
                        elif tokens[i+4] in months:
                            try:
                                if int(tokens[i+6]) in range(1970,2025):
                                    list_of_dates.append(''.join(tokens[i:i+7]))
                                elif int(tokens[i+6]) in range(0,100):
                                    list_of_dates.append(''.join(tokens[i:i+7]))
                                else:
                                    pass
                            except:
                                pass
                        else:
                            pass
                    elif tokens[i+4] == 'to':
                        if tokens[i+6] in ['current', 'present', 'today']:
                            list_of_dates.append(''.join(tokens[i:i+7]))
                        elif tokens[i+6] in months:
                            try:
                                if int(tokens[i+8]) in range(1970,2025):
                                    list_of_dates.append(''.join(tokens[i:i+9]))
                                elif int(tokens[i+8]) in range(0,100):
                                    list_of_dates.append(''.join(tokens[i:i+9]))
                                else:
                                    pass
                            except:
                                pass
                        else:
                            pass

                elif int(tokens[i+2]) in range(0,100):
                    if tokens[i+3] == ' - ':
                        if tokens[i+4] in ['current', 'present', 'today']:
                            list_of_dates.append(''.join(tokens[i:i+5]))
                        elif tokens[i+4] in months:
                            try:
                                if int(tokens[i+6]) in range(1970,2025):
                                    list_of_dates.append(''.join(tokens[i:i+7]))
                                elif int(tokens[i+6]) in range(0,100):
                                    list_of_dates.append(''.join(tokens[i:i+7]))
                                else:
                                    pass
                            except:
                                pass
                        else:
                            pass
                    elif tokens[i+4] == 'to':
                        if tokens[i+6] in ['current', 'present', 'today']:
                            list_of_dates.append(''.join(tokens[i:i+7]))
                        elif tokens[i+6] in months:
                            try:
                                if int(tokens[i+8]) in range(1970,2025):
                                    list_of_dates.append(''.join(tokens[i:i+9]))
                                elif int(tokens[i+8]) in range(0,100):
                                    list_of_dates.append(''.join(tokens[i:i+9]))
                                else:
                                    pass
                            except:
                                pass
                        else:
                            pass

            except:
                pass
    return(list_of_dates)

import xlrd
import pandas as pd


def travel_dataset_xls_preprocessing(path):
    xls_file = xlrd.open_workbook(f"{path}/data/travel.xls")
    sheet = xls_file.sheet_by_index(0)
    cases = []
    for row_index in range(sheet.nrows):
        row = sheet.row_values(row_index)
        if row[1] == 'case':
            case = []
        elif row[1] in ['JourneyCode:', 'HolidayType:', 'Price:', 'NumberOfPersons:',
                        'Region:', 'Transportation:', 'Duration:', 'Season:', 'Accommodation:', 'Hotel:']:
            value = row[2]
            if isinstance(value, str) and (value.endswith(',') or value.endswith('.')):
                value = value[:-1]
            case.append(value)
        if row[1] == 'Hotel:':
            cases.append(case)
            print(case)

    df = pd.DataFrame(cases)
    df.columns = ['id', 'holiday-type', 'price', 'num-persons', 'region', 'transportation', 'duration', 'season',
                  'accomodation', 'hotel']
    print(df)
    df.to_csv(f'{path}/data/travel.csv', index=False)


travel_dataset_xls_preprocessing("/Users/clararivadulla/Repositories/SEL-PW3")

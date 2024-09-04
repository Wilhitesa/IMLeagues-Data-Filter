# Press ⌃R to execute it.
import csv
from warnings import catch_warnings

# Important initializations. used for filenames.
fulldata_filename = 'FullNormalData.csv'
filter_filename = 'DataFilter.csv'
final_filename = 'RemainderRows.csv'

#fields = []
with open(final_filename, 'w') as final_file:
    print('Attempting file filtering...')
    final_file_csv = csv.writer(final_file)
    with open(fulldata_filename, 'r') as fulldata_file:
        # Create CSV file. Find the index of the ID field for future use.
        fulldata_csv = csv.reader(fulldata_file)
        fields = next(fulldata_csv)
        final_file_csv.writerow(fields)
        id_index_full = fields.index('ASU ID')
        year_index = fields.index('Grad Year')

        # Iterate through each row in the full data
        for row in fulldata_csv:
            # Retrieve the ID in the row.
            #fulldata_row = next(fulldata_csv)
            fulldata_id = row[id_index_full]

            try:
                if int(row[year_index]) <= 2024:
                    continue
            except:
                print('Issue occurred with entry {fname} {lname}. Year given: {year}'.format(fname = row[2], lname = row[3], year = row[year_index]))
                continue

            # Open the filter file. Find the index of the ID field as well.
            with open(filter_filename, 'r') as filter_file:
                filterdata_csv = csv.reader(filter_file)
                filter_fields = next(filterdata_csv)
                id_index_filtered = filter_fields.index('ASU ID')
                in_filter = False

                # Run through the entire file. If the IDS match, move to the next name.
                # In other words, name already exists in the filter file.
                for filter_row in filterdata_csv:
                    #filterdata_row = next(filterdata_csv)
                    filterdata_id = filter_row[id_index_filtered]
                    if fulldata_id == filterdata_id:
                        in_filter = True
                        break

                if not in_filter:
                    final_file_csv.writerow(row)
    print('\nall filtered entries successfully transferred to {filename}.'.format(filename = final_filename))
# Press ⌃R to execute it.
import csv

# Important initializations. used for filenames.
fulldata_filename = 'FullNormalData.csv'
filter_filename = 'DataFilter.csv'
final_filename = 'RemainderRows.csv'

#fields = []

with open(fulldata_filename, 'r') as fulldata_file:
    # Create CSV file. Find the index of the ID field for future use.
    fulldata_csv = csv.reader(fulldata_file)
    fields = next(fulldata_csv)
    id_index_full = fields.index('ASU ID')

    # Iterate through each row in the full data
    for row in fulldata_csv:
        # Retrieve the ID in the row.
        #fulldata_row = next(fulldata_csv)
        fulldata_id = row[id_index_full]

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
                if(fulldata_id == filterdata_id):
                    in_filter = True
                    break

            if not in_filter:
                print(row)

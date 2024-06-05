from bs4 import BeautifulSoup

# Create a new BeautifulSoup object with an empty HTML document
html = BeautifulSoup(features="html.parser")
html.append(html.new_tag('html'))
html.html.append(html.new_tag('body'))

# Create the main table
main_table = html.new_tag('table')

# Add 17 rows to the main table
for i in range(1, 18):
    # Create a new row
    row = html.new_tag('tr')

    # Add the row number in the first cell
    row_number = html.new_tag('td')
    row_number.string = str(i)
    row.append(row_number)

    # Create a 2x1 table in the second cell
    nested_table = html.new_tag('table')
    nested_row1 = html.new_tag('tr')
    nested_cell1 = html.new_tag('td')
    nested_cell1.string = 'Text data'
    nested_cell2 = html.new_tag('td')

    # Create a 4x1 table of images in the first cell
    images_table1 = html.new_tag('table')
    for _ in range(4):
        image_row = html.new_tag('tr')
        for _ in range(1):
            image_cell = html.new_tag('td')
            image = html.new_tag('img', src='/home/yashodhan/Documents/Research_projects/NewVariableStars/results/starwise/1/MPA_lk.png')
            image_cell.append(image)
            image_row.append(image_cell)
        images_table1.append(image_row)
    nested_cell1.append(images_table1)

    # Create a 4x4 table of images in the second cell
    images_table2 = html.new_tag('table')
    for _ in range(4):
        image_row = html.new_tag('tr')
        for _ in range(4):
            image_cell = html.new_tag('td')
            image = html.new_tag('img', src='/home/yashodhan/Documents/Research_projects/NewVariableStars/results/starwise/1/MPA_lk.png')
            image_cell.append(image)
            image_row.append(image_cell)
        images_table2.append(image_row)
    nested_cell2.append(images_table2)

    # Add cells to the nested table row
    nested_row1.append(nested_cell1)
    nested_row1.append(nested_cell2)
    nested_table.append(nested_row1)

    # Add the nested table to the row
    row.append(nested_table)

    # Add the row to the main table
    main_table.append(row)

# Add the main table to the body of the HTML document
html.html.body.append(main_table)

# Save the HTML file
with open('table.html', 'w') as f:
    f.write(str(html))

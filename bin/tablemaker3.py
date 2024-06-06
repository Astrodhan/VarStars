from bs4 import BeautifulSoup
import os

# Create a new BeautifulSoup object with an empty HTML document
html = BeautifulSoup(features="html.parser")
html.append(html.new_tag('html'))
html.html.append(html.new_tag('body'))

# Create the outer table (17 x 2)
outer_table = html.new_tag("table")
for i in range(1, 18):
    # Create a new row (tr)
    row = html.new_tag("tr")

    # First td contains the row number in text format
    row_number_td = html.new_tag("td")
    row_number_td.string = str(i)
    row.append(row_number_td)

    # Second td contains a 2 x 1 table
    inner_table_1 = html.new_tag("table")
    inner_table_1_row_1 = html.new_tag("tr")
    inner_table_1_row_1_td = html.new_tag("td")
    inner_table_1_row_1_td.string = f"Row {i} Data"
    inner_table_1_row_1.append(inner_table_1_row_1_td)
    inner_table_1_row_2 = html.new_tag("tr")
    inner_table_1_row_2_td = html.new_tag("td")
    inner_table_2 = html.new_tag("table")
    inner_table_1_row_2_td.append(inner_table_2)
    inner_table_1_row_2.append(inner_table_1_row_2_td)
    inner_table_1.append(inner_table_1_row_1)
    inner_table_1.append(inner_table_1_row_2)
    row.append(inner_table_1)

    # Append the row to the outer table
    outer_table.append(row)

    # Create a 4 x 1 table of images for the second td in inner_table_1_row_2
    inner_table_2_row_1 = html.new_tag("tr")
    inner_table_2_row_1_td = html.new_tag("td")
    for _ in range(4):
        image_path = "path/to/image.jpg"  # Path to your image file
        if os.path.exists(image_path):
            img = html.new_tag("img", src=image_path)
            inner_table_2_row_1_td.append(img)
    inner_table_2_row_1.append(inner_table_2_row_1_td)

    # Create a 4 x 4 table of images for the second td in inner_table_1_row_2
    inner_table_2_row_2 = html.new_tag("tr")
    inner_table_2_row_2_td = html.new_tag("td")
    inner_table_2_row_2_td_inner_table = html.new_tag("table")
    for _ in range(4):
        inner_table_2_row = html.new_tag("tr")
        for _ in range(4):
            image_path = "path/to/image.jpg"  # Path to your image file
            if os.path.exists(image_path):
                img = html.new_tag("img", src=image_path)
                inner_table_2_row.append(html.new_tag("td", img))
        inner_table_2_row_2_td_inner_table.append(inner_table_2_row)
    inner_table_2_row_2_td.append(inner_table_2_row_2_td_inner_table)
    inner_table_2_row_2.append(inner_table_2_row_2_td)
    inner_table_2.append(inner_table_2_row_1)
    inner_table_2.append(inner_table_2_row_2)

# Add the outer table to the HTML document
html.body.append(outer_table)

# Write the HTML to a file
with open("output.html", "w") as file:
    file.write(str(html))

from bs4 import BeautifulSoup

# Create a new BeautifulSoup object
soup = BeautifulSoup(features="html.parser")

# Create the main table
table = soup.new_tag('table')

# Add rows to the table
for i in range(17):
    tr = soup.new_tag('tr')
    
    # First column in the row containing the row number
    td1 = soup.new_tag('td')
    td1.string = f'Row {i+1}'
    tr.append(td1)
    
    # Second column in the row containing a 2x1 table
    td2 = soup.new_tag('td')
    sub_table = soup.new_tag('table')
    
    # First row in the sub-table containing text data
    sub_tr1 = soup.new_tag('tr')
    sub_td1 = soup.new_tag('td')
    sub_td1.string = 'Text Data'
    sub_tr1.append(sub_td1)
    sub_table.append(sub_tr1)
    
    # Second row in the sub-table containing a 1x2 table
    sub_tr2 = soup.new_tag('tr')
    sub_td2 = soup.new_tag('td')
    
    # 1x4 table of images in the first column
    img_table1 = soup.new_tag('table')
    for _ in range(4):
        img_tr = soup.new_tag('tr')
        for _ in range(4):
            img_td = soup.new_tag('td')
            img = soup.new_tag('img', src='eg.png', width='50', height='50')
            img_td.append(img)
            img_tr.append(img_td)
        img_table1.append(img_tr)
    sub_td2.append(img_table1)
    
    # 4x4 table of images in the second column
    img_table2 = soup.new_tag('table')
    for _ in range(4):
        img_tr = soup.new_tag('tr')
        for _ in range(4):
            img_td = soup.new_tag('td')
            img = soup.new_tag('img', src='eg.png', width='50', height='50')
            img_td.append(img)
            img_tr.append(img_td)
        img_table2.append(img_tr)
    sub_td2.append(img_table2)
    
    sub_tr2.append(sub_td2)
    sub_table.append(sub_tr2)
    
    td2.append(sub_table)
    tr.append(td2)
    
    table.append(tr)

# Append the table to the body of the HTML document
soup.append(table)

# Save the HTML to a file
with open('output.html', 'w') as file:
    file.write(soup.prettify())


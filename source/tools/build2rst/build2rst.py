""" 
Usage: 

Basic CLI Format: 
    python build2rst.py --location /Users/username/nccoe-tls-visibility/source --stem demscenario --template /Users/username/nccoe-tls-visibility/ds_template.jinja2 ds.xlsx

With default template and stem: 
    python build2rst.py --location /Users/username/nccoe-tls-visibility/source ds.xlsx

With root path: 
    python build2rst.py --root /Users/username/nccoe-tls-visibility --location source --stem demscenario --template my_template.jinja2 ds.xlsx

With only root and location: 
    python build2rst.py --root /Users/username/nccoe-tls-visibility --location source ds.xlsx

With custom template and default stem: 
    python build2rst.py --location /Users/username/nccoe-tls-visibility/source --template /Users/username/nccoe-tls-visibility/custom_template.jinja2 ds.xlsx

"""

from functools import reduce
import os
from pathlib import Path
import click
import openpyxl

LARGEST_TABLE_SIZE = 10
MAX_NUM_SCREENSHOTS = 20
def lengthen_shorten(tag, value):
    value = str(value)
    if "_LEN_" in tag:
        splitted = tag.split('_')
        desired_length = int(splitted[-1])
        if (desired_length < len(value)):
            print(f"Error: {tag} length not long enough for value {value}.")
            return '_'.join(splitted[:-2]), value[:desired_length]
        else:
            return '_'.join(splitted[:-2]), value + (desired_length - len(value)) * ' '
    else:
        return tag, value


def gen_tables(template_lines, current_row, row_names):
    replacer = {}
    for line in template_lines:
        if line.startswith("ENUMERATE"):
            fields = line.strip().split('_')[1:]
            table = ""
            table_title_1 = ""
            table_title_2 = ""
            table_title_3 = ""

            for f in fields:
                for r in range(len(row_names)):
                    tag, value = lengthen_shorten(row_names[r], current_row[r])
                    #print("CHECKING TITLE:", tag, f)
                    if (tag == f + "_TITLE"):
                        print("CHECKING TITLE:", tag, f, value)
                        table_title_1 += '+-' + len(value + ' ')*'-'
                        table_title_2 += '| ' + value + ' '
                        table_title_3 += '+=' + len(value + ' ')*'='
            if (table_title_1 != ""):
                table_title_1 += "+"
                table_title_2 += "|"
                table_title_3 += "+"
                table += table_title_1 + "\n" + table_title_2 + "\n" + table_title_3 + "\n"
            print(table)
            for k in range(0,LARGEST_TABLE_SIZE):
                table_line = ""
                table_line_2 = ""
                for f in fields:
                    for r in range(len(row_names)):
                        if (current_row[r] != None):
                            tag, value = lengthen_shorten(row_names[r], current_row[r])
                            if tag == f + str(k) :
                                table_line += '| ' + value + ' '
                                table_line_2 += '+-' + len(value+' ') * '-' 
                if (table_line != ""):
                    table_line += "|" 
                    table_line_2 += "+"
                    table += table_line + "\n" + table_line_2 + "\n"
            replacer[line.strip()] = table[:-1]
    return replacer

def screenshots(row, row_names, loc='tools/build2rst/screenshot-template.rst'):
    with open(loc, 'r') as f:
        template = f.read()

    out = ""
    for m in range(0,MAX_NUM_SCREENSHOTS+1):
        curr = template
        addme = False
        indent = False
        for n in range(len(row_names)):
            #print(row_names[n])
            if ("Screenshot" in row_names[n]):
                if (row_names[n][-1] == str(m) and row[n] != None):
                    if "INDENT:" in str(row[n]):
                        indent = True
                    curr = curr.replace(f"[[{row_names[n][:-1]}]]", str(row[n]).replace("INDENT:", ""))
                    addme = True
        if (addme):
            if (indent):
                curr = curr.replace("[[spaces]]", "   ")
            else:
                curr = curr.replace("[[spaces]]", "")
            curr += "\n\n"
            out += curr
    return out

def perform_replacement(row, replacers, rst_content, template_lines, data):

    table_replacer = gen_tables(template_lines, row, data[0])
    for k in table_replacer.keys():
        rst_content = rst_content.replace(k, table_replacer[k])

    #print(rst_content)
    rst_content = rst_content.replace("REPLACE_WITH_SCREENSHOTS", screenshots(row, data[0]))
    #print(rst_content)
    for k in range(10): # if we replace things multiple times, we can replace [[]] references in the cells of the workbook
        for r in replacers.keys():
            if row[r] != None:
                #print(f"[[{replacers[r]}]]")
                if k == 0:
                    tag, value = lengthen_shorten(replacers[r], row[r])
                else:
                    tag = str(replacers[r])
                    value = str(row[r])

                if tag.endswith("_RST") and f"[[{tag[:-4]}]]" in rst_content:
                    with open('tools/build2rst/templates/' + value, 'r') as read_rst:
                        readvalue = read_rst.read()
                    with open('tools/build2rst/templates/' + value, 'r') as read_rst_lines:
                        lines = read_rst_lines.readlines()
                    value = perform_replacement(row, replacers, readvalue, lines, data)
                    tag = tag[:-4]
                    
                rst_content = rst_content.replace(f"[[{tag}]]", value)
    return rst_content



@click.command()
@click.argument('xlsx_file', type=click.Path(exists=True))
@click.option('--location', required=True, type=click.Path(), help='Location to write generated RST files.')
@click.option('--stem', default='server', help='Stem of the filenames for generated RST files.')
@click.option('--root', default=None, type=click.Path(), help='Root directory for resolving relative paths.')
@click.option('--template', default='server-template.rst', type=click.Path(), help='Location of template.')
def generate_rst_files(xlsx_file, location, stem, root, template):
    # Resolve paths if root is provided
    if root:
        click.echo(f"[Root location provided, relative paths will be resolved to '{root}'].")
        location = os.path.join(root, location)
        xlsx_file = os.path.join(root, xlsx_file)
    else:
        click.echo("[No root location provided, all inputs must be provided as absolute paths.]")

    # Ensure the output location exists
    os.makedirs(location, exist_ok=True)

    # Read Excel file
    click.echo(f"Reading XLSX file: {xlsx_file}")
    workbook = openpyxl.load_workbook(xlsx_file)
    sheet = workbook["1"]
    data = [list(row) for row in sheet.iter_rows(values_only=True)]
    data = [row for row in data if row[0] != None]

    click.echo(f"Excel file '{xlsx_file}' processed, {len(data)} scenarios read.")

    replacers = {k:data[0][k] for k in range(len(data[0]))}

    
    print(replacers)
    # Generate RST files
    generated_files = []

    with open(template, 'r') as templ_file:
        template_contents = templ_file.read()
    with open(template, 'r') as templ_file:
        template_lines = templ_file.readlines()


    filename_location = None
    for n in range(len(data[0])):
        if data[0][n] == "Filename":
            filename_location = n


    for i, row in enumerate(data):
        print(row)
        if i != 0:
            rst_content = template_contents



            # replace something like [[Description]] with the value of the "Description" column
            rst_content = perform_replacement(row, replacers, rst_content, template_lines, data)

            if filename_location == None or row[filename_location] == None:
                output_filename = f"{stem}-{i}.rst"
            else:
                output_filename = f"{row[filename_location]}.rst"
            output_path = os.path.join(location, output_filename)
            with open(output_path, 'w') as output_file:
                output_file.write(rst_content)

            click.echo(f"Generating file '{output_filename}'.")
            generated_files.append(output_filename)
    
    
    # Generate aggregation RST file
    index_filename = f"{stem}-index.rst"
    index_path = os.path.join(location, index_filename)
    
    with open(index_path, 'w') as index_file:
        index_file.write(".. toctree::\n   :maxdepth: 1\n\n")
        for file in generated_files:
            index_file.write(f"   /{str(Path(location) / file)}\n")
    click.echo(f"Generating aggregation file, '{index_filename}'.")
    click.echo("\nComplete.")

if __name__ == '__main__':
    generate_rst_files()
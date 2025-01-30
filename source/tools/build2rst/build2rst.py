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

def lengthen_shorten(tag, value):
    value = str(value)
    if "_LEN_" in tag:
        splitted = tag.split('_')
        desired_length = int(splitted[-1])
        if (desired_length < len(value)):
            print(f"Error: {tag} length not long enough for value {value}.")
            return splitted[0], value[:desired_length]
        else:
            return splitted[0], value + (desired_length - len(value)) * ' '
    else:
        return tag, value


def gen_tables(template_lines, current_row, row_names):
    replacer = {}
    for line in template_lines:
        if line.startswith("ENUMERATE"):
            fields = line.strip().split('_')[1:]
            table = ""
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
    sheet = workbook.active
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

    for i, row in enumerate(data):
        print(row)
        if i != 0:
            rst_content = template_contents

            table_replacer = gen_tables(template_lines, row, data[0])
            for k in table_replacer.keys():
                rst_content = rst_content.replace(k, table_replacer[k])

            # replace something like [[Description]] with the value of the "Description" column
            for r in replacers.keys():
                if row[r] != None:
                    print(f"[[{replacers[r]}]]")

                    tag, value = lengthen_shorten(replacers[r], row[r])
                    rst_content = rst_content.replace(f"[[{tag}]]", value)

            output_filename = f"{stem}-{i}.rst"
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
""" 
Usage: 

Basic CLI Format: 
    python dem2rst.py --location /Users/username/nccoe-tls-visibility/source --stem demscenario --template /Users/username/nccoe-tls-visibility/ds_template.jinja2 ds.xlsx

With default template and stem: 
    python dem2rst.py --location /Users/username/nccoe-tls-visibility/source ds.xlsx

With root path: 
    python dem2rst.py --root /Users/username/nccoe-tls-visibility --location source --stem demscenario --template my_template.jinja2 ds.xlsx

With only root and location: 
    python dem2rst.py --root /Users/username/nccoe-tls-visibility --location source ds.xlsx

With custom template and default stem: 
    python dem2rst.py --location /Users/username/nccoe-tls-visibility/source --template /Users/username/nccoe-tls-visibility/custom_template.jinja2 ds.xlsx

"""

from functools import reduce
import os
from pathlib import Path
import click
import openpyxl

def format_rst_content(scenario_id, title, purpose, description, procedure, expected, screenshot, passive_tests, active_tests):
    title = f"Scenario {scenario_id}: {title}"

    results = [[passive_tests[k][kk] for kk in passive_tests[k].keys()] for k in passive_tests.keys()] + [[active_tests[k][kk] for kk in active_tests[k].keys()] for k in active_tests.keys()]
    
    results = [
        passive_tests['bounded_life_time']['real_time'],
        passive_tests['bounded_life_time']['post_facto'],
        passive_tests['exported_session_key']['real_time'],
        passive_tests['exported_session_key']['post_facto'],
        active_tests['break_and_inspect_mira']['real_time'],
        active_tests['break_and_inspect_mira']['post_facto'],
        active_tests['break_and_inspect_f5']['real_time'],
        active_tests['break_and_inspect_f5']['post_facto']
    ]
    results_out = [f"{results[n]}{' '*(len('Real-Time' if n % 2 == 0 else 'Post-Facto')-len(results[n]))}" for n in range(len(results))]
    
    results_str = ' | '.join(results_out)
    rst_content = f""".. _scenario-{scenario_id}:

{title}
{'=' * len(title)}

Purpose
-------

{purpose or "No purpose provided."}

Description
-----------

{description or "No description provided."}

Procedure
---------

{procedure or "No procedure provided."}

Expected Outcome
----------------

{expected or "No expected outcome provided."}

+-------------------------------------------------+-------------------------------------------------+
| Passive                                         | Active                                          |
+------------------------+------------------------+------------------------+------------------------+
| Bounded Life-Time      | Exported Session Key   | Break & Inspect (Mira) | Break and Inspect (F5) |
+-----------+------------+-----------+------------+-----------+------------+-----------+------------+
| Real-Time | Post-Facto | Real-Time | Post-Facto | Real-Time | Post-Facto | Real-Time | Post-Facto |
+===========+============+===========+============+===========+============+===========+============+
| {results_str} | 
+-----------+------------+-----------+------------+-----------+------------+-----------+------------+

Screenshots
-----------

{screenshot or "No screenshot provided."}


"""
    return rst_content

        

def format_screenshots(screenshot_cell, screenshot_caption_cell, screenshot_alt_text_cell):
    screens = screenshot_cell.split(',')
    captions = screenshot_caption_cell.split('//')
    alts = screenshot_alt_text_cell.split('//')
    screens = [s.strip() for s in screens]
    captions = [s.strip() for s in captions]
    alts = [s.strip() for s in alts]
    rst_out = ""
    for k in range(len(screens)):
        rst_content = f"""

.. figure:: /images/demonstration_results/{screens[k]}
   :width: 90%
   :alt: {alts[k]}

   {captions[k]}

"""
        rst_out += rst_content
    return rst_out

@click.command()
@click.argument('xlsx_file', type=click.Path(exists=True))
@click.option('--location', required=True, type=click.Path(), help='Location to write generated RST files.')
@click.option('--stem', default='ds', help='Stem of the filenames for generated RST files.')
@click.option('--root', default=None, type=click.Path(), help='Root directory for resolving relative paths.')
def generate_rst_files(xlsx_file, location, stem, root):
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
    data = [list(row) for row in sheet.iter_rows(values_only=True)][3:]  # Skip the first three header rows
    data = [row for row in data if row[0] != None]
    click.echo(f"Excel file '{xlsx_file}' processed, {len(data)} scenarios read.")

    scenario_list = []

    # Generate RST files
    generated_files = []
    for i, row in enumerate(data):
        scenario_id = row[0] or f"Scenario {i + 1}"  # Use scenario ID or default to index
        title = row[1]
        purpose = row[2]
        description = row[3]
        procedure = row[4]
        expected = row[5]
        screenshot = row[14]
        screenshotNotes = row[15]
        screenshotAlts = row[16]

        passive_tests = {
            'bounded_life_time': {'real_time': row[6], 'post_facto': row[7]},
            'exported_session_key': {'real_time': row[8], 'post_facto': row[9]}
        }

        active_tests = {
            'break_and_inspect_mira': {'real_time': row[10], 'post_facto': row[11]},
            'break_and_inspect_f5': {'real_time': row[12], 'post_facto': row[13]}
        }

        #print(gen_grid_table([['Passive', 'Active'],['Break and Inspect (MIRA)', 'Break and Inspect (F5)', 'Bounded Life-Time', 'Exported Session Key'], ['Real Time', 'Post-Facto']], ['Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass']))

        one_screen = format_screenshots(screenshot_cell=screenshot, screenshot_caption_cell=screenshotNotes, screenshot_alt_text_cell=screenshotAlts)

        rst_content = format_rst_content(
            scenario_id, title, purpose, description, procedure, expected, one_screen, passive_tests, active_tests
        )

        output_filename = f"{stem}-{i + 1}.rst"
        output_path = os.path.join(location, output_filename)
        with open(output_path, 'w') as output_file:
            output_file.write(rst_content)
        click.echo(f"Generating file '{output_filename}'.")
        generated_files.append(output_filename)
        scenario_list += [f'* Scenario {scenario_id}: :ref:`scenario-{scenario_id}`\n']
    # Generate aggregation RST file
    index_filename = f"{stem}-index.rst"
    index_path = os.path.join(location, index_filename)
    with open(index_path, 'w') as index_file:
        index_file.write(".. toctree::\n   :maxdepth: 1\n\n")
        for file in generated_files:
            index_file.write(f"   /{str(Path(location) / file)}\n")
        # index_file.write("\nIncluded Files:\n===============\n\n")
        #for scenario in scenario_list:
        #    index_file.write(scenario)
    click.echo(f"Generating aggregation file, '{index_filename}'.")

    click.echo("\nComplete.")

if __name__ == '__main__':
    generate_rst_files()
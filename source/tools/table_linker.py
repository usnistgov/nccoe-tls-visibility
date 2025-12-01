import urllib.parse
table = '''
+--------------------------------------------------------------------------------+
| Configuration Files                                                            |
+================================================================================+
| /home/administrator/testapp-stack/testapp-build/testapp/oidc-client-secret.txt |
+--------------------------------------------------------------------------------+
| /home/administrator/testapp-stack/testapp-build/testapp/testapp.py             |
+--------------------------------------------------------------------------------+
| /home/administrator/testapp-stack/testapp-build/Dockerfile                     |
+--------------------------------------------------------------------------------+
| /home/administrator/testapp-stack/testapp-build/pyenv.cfg                      |
+--------------------------------------------------------------------------------+
| /home/administrator/testapp-stack/testapp-build/requirements.txt               |
+--------------------------------------------------------------------------------+
| /home/administrator/testapp-stack/docker-compose.yml                           |
+--------------------------------------------------------------------------------+
| /home/administrator/testapp-stack/nginx-default.conf                           |
+--------------------------------------------------------------------------------+
| /etc/eva/eva-openssl.cnf                                                       |
+--------------------------------------------------------------------------------+
| /etc/eva/eva.conf                                                              |
+--------------------------------------------------------------------------------+
'''

title = 'Configuration Files'

url = 'https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build'

folder = 'tls-servers/Bounded-lifetime Rotated EDH Server Key Build/testapp-server'

new_rows = []
maxlen = 0
for row in table.splitlines():
    linkable = len(row) > 0 and '----' not in row and '====' not in row and not title in row

    if linkable:
        path = row.replace('|', '').strip()
        new_url = urllib.parse.quote(f"{folder}{path}")
        new_row = f"`{path} <{url}/{new_url}>`__"
        maxlen = max(len(new_row), maxlen)
        new_rows.append(new_row)

print(f'+-{'-'*maxlen}-+')
print(f'| {title}{' '*(maxlen-len(title))} |')
print(f'+={'='*maxlen}=+')
for r in new_rows:
    print(f'| {r}{' '*(maxlen-len(r))} |')
    print(f'+-{'-'*maxlen}-+')

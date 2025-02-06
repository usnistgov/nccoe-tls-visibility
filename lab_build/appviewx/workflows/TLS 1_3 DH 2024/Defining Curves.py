import SSH_Helper

curves = ['prime256v1', 'secp384r1', 'secp521r1']
cmd = list()

hsm_server = "<%hsmServer%>"

gateway_base_url, gateway_key = SSH_Helper.fetch_gateway_properties()
session_id = "<%sessionId%>"

hsm_ip = SSH_Helper.execute_query_explorer(session_id, gateway_base_url, gateway_key, "TLS - Fetch IP Address", hook_input = {"serverName":hsm_server})[0]["ip"]

hsm_username = "$$SSM.username$$"
hsm_password = "$$SSM.password$$"

AVX::OUTPUT({'curvesList':curves, 'cmd': cmd, 'hsm_ip': hsm_ip, 'hsm_username': hsm_username, 'hsm_password': hsm_password})
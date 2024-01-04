import nmap3

def perform_port_scan(target):
    nmap_discovery = nmap3.NmapHostDiscovery()
    scan_output = nmap_discovery.nmap_portscan_only(target)
    return scan_output

def sanitize_scan_results(scan_results):
    keys_to_sanitize = ["runtime", "stats", "task_results"]
    sanitized_results = scan_results.copy()
    for key_to_remove in keys_to_sanitize:
        sanitized_results.pop(key_to_remove, None)
    return sanitized_results

def check_production_endpoints(scan_results):
    for host, scan_result in scan_results.items():
        if scan_result['state']['state'] == 'up':
            print(f"The production endpoint {host} is reachable.")

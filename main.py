from utils import perform_port_scan, sanitize_scan_results, check_production_endpoints

target_ip = "192.168.1.1/32"
scan_output = perform_port_scan(target_ip)

sanitized_results = sanitize_scan_results(scan_output)

check_production_endpoints(sanitized_results)

import logging
from utils import perform_nmap_scan, sanitize_scan_results, check_production_endpoints
from typing import Dict
from os import environ

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    target_ips = environ.get("TARGET_IPS", "192.168.1.0/24").split(',')

    try:
        for target_ip in target_ips:
            scan_output: Dict[str, Dict] = perform_nmap_scan(target_ip)
            sanitized_results: Dict[str, Dict] = sanitize_scan_results(scan_output)
            check_production_endpoints(sanitized_results)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

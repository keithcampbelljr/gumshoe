import logging
from utils import perform_nmap_scan, sanitize_scan_results, check_production_endpoints
from typing import Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    target_ip: str = "192.168.1.0/24"
    
    try:
        scan_output: Dict[str, Dict] = perform_nmap_scan(target_ip)
        sanitized_results: Dict[str, Dict] = sanitize_scan_results(scan_output)
        check_production_endpoints(sanitized_results)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

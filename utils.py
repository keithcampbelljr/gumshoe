import logging
import nmap3
from typing import Dict

logger = logging.getLogger(__name__)

def perform_nmap_scan(target: str) -> Dict[str, Dict]:
    """
    Perform an Nmap scan on the specified target.

    Args:
        target (str): The target IP address or range.

    Returns:
        Dict[str, Dict]: Nmap scan results.
    """
    nmap_discovery = nmap3.NmapHostDiscovery()
    scan_output: Dict[str, Dict] = nmap_discovery.nmap_no_portscan(target)
    return scan_output

def sanitize_scan_results(scan_results: Dict[str, Dict]) -> Dict[str, Dict]:
    """
    Remove unnecessary information from Nmap scan results.

    Args:
        scan_results (Dict[str, Dict]): Nmap scan results.

    Returns:
        Dict[str, Dict]: Sanitized scan results.
    """
    keys_to_sanitize = ["runtime", "stats", "task_results"]
    sanitized_results: Dict[str, Dict] = scan_results.copy()
    for key_to_remove in keys_to_sanitize:
        sanitized_results.pop(key_to_remove, None)
    return sanitized_results

def check_production_endpoints(scan_results: Dict[str, Dict]) -> None:
    """
    Check the status of production endpoints based on Nmap scan results.

    Args:
        scan_results (Dict[str, Dict]): Nmap scan results.
    """
    for host, scan_result in scan_results.items():
        if scan_result['state']['state'] == 'up':
            logger.info(f"The production endpoint {host} is reachable.")

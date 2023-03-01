import os
from msedge.selenium_tools import Edge, EdgeOptions
from setup import get_options

def get_driver(executable_path: str = "msedgedriver.exe"):
    """
    Returns an instance of the Edge web driver with options obtained from the `get_options()` function.
    
    :param executable_path: Path to the Microsoft Edge WebDriver executable.
    :type executable_path: str
    
    :return: An instance of the Edge web driver.
    :rtype: msedge.selenium_tools.Edge
    """
    options = get_options()

    if not executable_path:
        raise ValueError("Executable path is required.")
    if not os.path.exists(executable_path):
        raise FileNotFoundError(f"Driver not found: {executable_path}")
        
    driver = Edge(executable_path=executable_path, options=options)
    return driver

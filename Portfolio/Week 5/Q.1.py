'''Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used'''

import platform

def get_operating_system():
    system_info = platform.system()
    return system_info

if __name__ == "__main__":
    os = get_operating_system()
    print(f"The operating system is: {os}")
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""______    _          _ ______            
 |  ____|  (_)        | |  ____|           
 | |__ _ __ _  ___  __| | |__   __ _  __ _ 
 |  __| '__| |/ _ \/ _` |  __| / _` |/ _` |
 | |  | |  | |  __/ (_| | |____ (_| | (_| |
 |_|  |_|  |_|\___|\__,_|______\__, |\__, |
                                __/ | __/ |
                               |___/ |___/
The FriedEgg contributors, (c) 2021."""
import os
import sys

print("______    _          _ ______ "           
 "\n|  ____|  (_)        | |  ____| "          
 "\n| |__ _ __ _  ___  __| | |__   __ _  __ _ "
 "\n|  __| '__| |/ _ \/ _` |  __| / _` |/ _` |"
 "\n| |  | |  | |  __/ (_| | |____ (_| | (_| |"
 "\n|_|  |_|  |_|\___|\__,_|______\__, |\__, |"
 "\n                               __/ | __/ |"
 "\n                              |___/ |___/"
"\nThe FriedEgg contributors, (c) 2021."
"\nMade with <3 using Python & Django!")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'friedegg.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

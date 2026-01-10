# habcup_manual.py
from parts.hubcaps import is_hubcaps_on_the_wheel, is_hubcap_hit_boundaries

usr_choice = bool(input("T/F: "))

is_hubcap_hit_boundaries(usr_choice)
is_hubcaps_on_the_wheel(usr_choice)

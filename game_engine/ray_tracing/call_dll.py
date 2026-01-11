# call_dll.py
from ctypes import CDLL

rays = CDLL(r"D:\\beamng\\game_engine\\ray_tracing\\./rays.dll")

rays.generate_rays()

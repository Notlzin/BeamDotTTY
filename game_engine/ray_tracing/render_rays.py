# render_rays.py
from time import sleep

def render_rays_py():
    while True:
        for i in range(5):
            print(f"[RAYTRACE] Rendered ray: #{i} currently.")
            sleep(0.256)

if __name__ == "__main__":
    render_rays_py()

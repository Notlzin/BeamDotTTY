# runProc.py
import subprocess

def runProc(option):
    try:
        if option.startswith("hwData"):
            result = subprocess.run(
                [r"D:\\beamng\\game_engine\\hw_acceleration\\hwData.exe"],
                capture_output=True,
                text=True
            )
            print(result.stdout)
        elif option.startswith("hwAccel"):
            result = subprocess.run(
                [r"D:\\beamng\\game_engine\\hw_acceleration\\hwAccel.exe"],
                capture_output=True,
                text=True,
            )
            print(result.stdout)
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    runProc("hwData")
    runProc("hwAccel")

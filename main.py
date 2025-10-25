import subprocess
import os
import math



cwd = os.getcwd()
swd = os.path.join(cwd, "getcpu.sh") # Script Working Directory




def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

#cpu_temp = run_cmd("vcgencmd measure_temp")
cpu_model = run_cmd("lscpu | grep 'Model name'").split(":", 1)[1].strip()
cpu_cores = run_cmd("lscpu | grep 'Core(s) per cluster:'").split(":", 1)[1].strip()
cpu_freq_percentage = run_cmd("lscpu | grep 'CPU(s) scaling MHz:'").split(":", 1)[1].strip()
cpu_freqs = run_cmd("cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq")
cpu_freqs_mhz = round(int(cpu_freqs.split("\n")[0]) // 1000, 1)
cpu_min_freq = run_cmd("lscpu | grep 'CPU min MHz:'").split(":", 1)[1].strip()
cpu_max_freq = run_cmd("lscpu | grep 'CPU max MHz:'").split(":", 1)[1].strip()

arch = run_cmd("uname -m")

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return int(f.read().strip()) / 1000
    except FileNotFoundError:
        return None

cpu_temp = round(get_cpu_temp(), 1)


print("CPU Temp:", cpu_temp)
print("CPU Model:", cpu_model)
print("CPU Cores:", cpu_cores)
print("CPU Frequency (%):", cpu_freq_percentage)
print("CPU Frequency (Mhz):", cpu_freqs_mhz)
print("CPU Minimum Frequency:", cpu_min_freq)
print("CPU Maximum Frequency:", cpu_max_freq)
print("Architecture:", arch)

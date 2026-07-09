"""
=========================================
JARVIS SYSTEM ENGINE V2
=========================================
"""

import os
import socket
import platform
import psutil


class System:

    def battery(self):
        battery = psutil.sensors_battery()
        if battery:
            return battery.percent
        return None

    def cpu(self):
        return psutil.cpu_percent(interval=1)

    def ram(self):
        return psutil.virtual_memory().percent

    def disk(self):
        return psutil.disk_usage("/").percent

    def hostname(self):
        return platform.node()

    def os_name(self):
        return platform.system()

    def os_version(self):
        return platform.version()

    def processor(self):
        return platform.processor()

    def ip(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except:
            return "Unavailable"

    def shutdown(self):
        os.system("shutdown /s /t 1")

    def restart(self):
        os.system("shutdown /r /t 1")

    def lock(self):
        os.system("rundll32.exe user32.dll,LockWorkStation")

    def sleep(self):
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    def open_task_manager(self):
        os.system("start taskmgr")

    def open_control_panel(self):
        os.system("control")

    def open_settings(self):
        os.system("start ms-settings:")


system = System()
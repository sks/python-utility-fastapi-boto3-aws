import psutil

def get_system_metrics():
    """
    This API get the system metrics (CPU, Memory, Disk, System health)
    based on CPU Threshold (configurable)
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    cpu_threshold = 10
    status = "High" if cpu_percent > cpu_threshold else "Healthy"

    return {
    "cpu_percentage" : cpu_percent,
    "mempry_percentage":memory_percent,
    "disk_percentage":disk_percent,
    "cpu_threshold":cpu_threshold,
    "system_status":status
    }




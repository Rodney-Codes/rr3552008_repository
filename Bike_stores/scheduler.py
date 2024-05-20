import schedule
import time
import subprocess

def run_python_scripts():
'''
    # List of Python scripts with their full paths
    scripts = [
        'C:/path/to/your/Py_aggregator.py', 
        'D:/another_path/to/second_script.py'
    ]
'''
   # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # List of Python scripts in the same directory
    scripts = [
        os.path.join(script_dir, 'Py_aggregator.py'), 
        os.path.join(script_dir, 'Py_data_QC.py')
    ]
    
    for script in scripts:
        # Run each script using subprocess.call
        subprocess.call(['python', script])

# Schedule the job to run at 10 AM every day
schedule.every().day.at("10:00").do(run_python_scripts)

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute if there's any scheduled task to run

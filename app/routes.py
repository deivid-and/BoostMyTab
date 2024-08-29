import subprocess
import os
import logging
from flask import Blueprint, render_template, jsonify
from flask_socketio import emit
import psutil
from . import socketio

logging.basicConfig(level=logging.DEBUG)

main = Blueprint('main', __name__)

def run_script(script_name, async_run=False):
    script_path = os.path.join(os.getcwd(), 'scripts', script_name)
    if not os.path.exists(script_path):
        error_msg = f"Script not found: {script_path}"
        logging.error(error_msg)
        return {"status": "error", "message": error_msg}
    
    try:
        logging.debug(f"Running script at path: {script_path}")
        
        if async_run:
            subprocess.Popen(
                [script_path],
                shell=True,
                cwd=os.path.dirname(script_path),
                env={**os.environ, 'PATH': os.path.join(os.getcwd(), 'scripts', 'adb') + os.pathsep + os.environ['PATH']}
            )
            success_message = f"Script {script_name} started successfully in the background."
            logging.debug(success_message)
            return {"status": "success", "message": success_message}
        else:
            result = subprocess.run(
                [script_path],
                capture_output=True, text=True, shell=True, check=True, cwd=os.path.dirname(script_path),
                timeout=120,
                env={**os.environ, 'PATH': os.path.join(os.getcwd(), 'scripts', 'adb') + os.pathsep + os.environ['PATH']}
            )
            if result.returncode == 0:
                success_message = f"Script executed successfully. Output: {result.stdout}"
                logging.debug(success_message)
                return {"status": "success", "message": success_message, "output": result.stdout}
            else:
                error_message = f"Script executed with errors. Error: {result.stderr}"
                logging.debug(error_message)
                return {"status": "error", "message": error_message, "output": result.stderr}
    except subprocess.TimeoutExpired:
        error_msg = "Script execution timed out."
        logging.error(error_msg)
        return {"status": "error", "message": error_msg}
    except subprocess.CalledProcessError as e:
        error_msg = f"Failed to execute script. Error: {e.stderr}"
        logging.error(error_msg)
        return {"status": "error", "message": error_msg}
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        logging.error(error_msg)
        return {"status": "error", "message": error_msg}

@main.route('/')
def index():
    logging.debug("Serving index page.")
    return render_template('index.html')

# Disable Unnecessary Processes
@main.route('/disable_google_bloatware', methods=['POST'])
def disable_google_bloatware():
    result = run_script('disable_google_bloatware.bat')
    return jsonify(result)

@main.route('/disable_samsung_bloatware', methods=['POST'])
def disable_samsung_bloatware():
    result = run_script('disable_samsung_bloatware.bat')
    return jsonify(result)

@main.route('/disable_misc_bloatware', methods=['POST'])
def disable_misc_bloatware():
    result = run_script('disable_misc_bloatware.bat')
    return jsonify(result)

@main.route('/disable_keyboard', methods=['POST'])
def disable_keyboard():
    result = run_script('disable_keyboard.bat')
    return jsonify(result)

# Performance Optimization
@main.route('/disable_power_saving', methods=['POST'])
def disable_power_saving():
    result = run_script('disable_power_saving.bat')
    return jsonify(result)

@main.route('/set_min_brightness', methods=['POST'])
def set_min_brightness():
    result = run_script('set_min_brightness.bat')
    return jsonify(result)

@main.route('/set_max_brightness', methods=['POST'])
def set_max_brightness():
    result = run_script('set_max_brightness.bat')
    return jsonify(result)

@main.route('/set_cpu_governor_performance', methods=['POST'])
def set_cpu_governor_performance():
    result = run_script('set_cpu_governor_performance.bat')
    return jsonify(result)

@main.route('/turn_off_animations', methods=['POST'])
def turn_off_animations():
    result = run_script('turn_off_animations.bat')
    return jsonify(result)

@main.route('/limit_background_processes', methods=['POST'])
def limit_background_processes():
    result = run_script('limit_background_processes.bat')
    return jsonify(result)

@main.route('/boost_wifi_network', methods=['POST'])
def boost_wifi_network():
    result = run_script('boost_wifi_network.bat')
    return jsonify(result)

# System Management
@main.route('/enter_recovery_mode', methods=['POST'])
def enter_recovery_mode():
    result = run_script('enter_recovery_mode.bat')
    return jsonify(result)

@main.route('/list_devices', methods=['POST'])
def list_devices():
    logging.debug("Received POST request for /list_devices")
    result = run_script('list_devices.bat')
    logging.debug(f"Response for /list_devices: {result}")
    return jsonify(result)

@main.route('/start_scrcpy', methods=['POST'])
def start_scrcpy():
    result = run_script('start_scrcpy.bat', async_run=True)
    return jsonify(result)

@main.route('/restart_tab', methods=['POST'])
def restart_tab():
    result = run_script('restart_tab.bat', async_run=True)
    return jsonify(result)

# Enable Unnecessary Processes
@main.route('/enable_google_bloatware', methods=['POST'])
def enable_google_bloatware():
    result = run_script('enable_google_bloatware.bat')
    return jsonify(result)

@main.route('/enable_samsung_bloatware', methods=['POST'])
def enable_samsung_bloatware():
    result = run_script('enable_samsung_bloatware.bat')
    return jsonify(result)

@main.route('/enable_misc_bloatware', methods=['POST'])
def enable_misc_bloatware():
    result = run_script('enable_misc_bloatware.bat')
    return jsonify(result)

@main.route('/enable_keyboard', methods=['POST'])
def enable_keyboard():
    result = run_script('enable_keyboard.bat')
    return jsonify(result)

# Performance Optimization
@main.route('/enable_power_saving', methods=['POST'])
def enable_power_saving():
    result = run_script('enable_power_saving.bat')
    return jsonify(result)

@main.route('/enable_battery_optimization', methods=['POST'])
def enable_battery_optimization():
    result = run_script('enable_battery_optimization.bat')
    return jsonify(result)

@main.route('/set_cpu_governor_balanced', methods=['POST'])
def set_cpu_governor_balanced():
    result = run_script('set_cpu_governor_balanced.bat')
    return jsonify(result)

@main.route('/turn_on_animations', methods=['POST'])
def turn_on_animations():
    result = run_script('turn_on_animations.bat')
    return jsonify(result)

@main.route('/unlimit_background_processes', methods=['POST'])
def unlimit_background_processes():
    result = run_script('unlimit_background_processes.bat')
    return jsonify(result)

@main.route('/reset_wifi_network', methods=['POST'])
def reset_wifi_network():
    result = run_script('reset_wifi_network.bat')
    return jsonify(result)

@socketio.on('connect')
def handle_connect():
    logging.debug('Client connected')
    emit_connected_devices()

@socketio.on('disconnect')
def handle_disconnect():
    logging.debug('Client disconnected')

def emit_connected_devices():
    logging.debug("Emitting connected devices")
    result = run_script('list_devices.bat')
    socketio.emit('device_list', {'output': result['message']})

from flask import Flask, request, jsonify
from jupyter_client import KernelManager
import os
import json

app = Flask(__name__)

# Initialize the Jupyter Kernel
km = KernelManager(kernel_name='python3')
km.start_kernel()
kc = km.client()
kc.start_channels()

@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.json
    code = data.get('code', '')
    
    # Execute code
    kc.execute(code)
    
    # Get output
    msg = kc.get_shell_msg()
    output = msg['content'].get('text/plain', 'No output returned')
    
    # Return output
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(port=5000)

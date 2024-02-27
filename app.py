from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Deployed'

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Retrieve the request data
        data = request.get_json()
        company_ticker = data.get('company_ticker')
        rev_growth = data.get('revenue_growth')

        if not company_ticker:
            return jsonify({'error': 'Company ticker not provided'}), 400

        # Execute the script with the provided input
        script_path = 'DCF-Indian-Equity-User-Input.py'
        process = subprocess.Popen(['python', script_path], 
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        
        # Provide input to the script
        input_data = f"{company_ticker}\n{rev_growth}\n"
        output, error = process.communicate(input=input_data.encode())
        result = output.decode('utf-8')

        if process.returncode != 0:
            return jsonify({'error': f'Script execution failed: {error.decode("utf-8")}', 'result': result}), 500

        return jsonify({'result': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

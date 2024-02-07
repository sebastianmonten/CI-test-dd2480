import os
from flask import Flask, request
import datetime

app = Flask(__name__)

def extract_basic_info(data):
    try:
        repo_name = data['repository']['name']
        pusher_name = data['pusher']['name']
        branch_ref = data['ref']
        commit_id = data['after']


        timestamp_str = data['head_commit']['timestamp']
        timestamp = datetime.datetime.fromisoformat(timestamp_str)
        date = timestamp.date()
        time = timestamp.time()
        
    except KeyError:
        return "Error: Requred data missing from json file!"

    
    return f"Repo: {repo_name}, Pusher: {pusher_name}, Branch: {branch_ref}, Timestamp: {date} {time}, Commit ID: {commit_id}"

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    data = request.json
    basic_info = extract_basic_info(data)
    # Get the directory of the current script and use it to create the log file path
    script_dir = os.path.dirname(os.path.realpath(__file__))
    log_file_path = os.path.join(script_dir, 'tmp', 'log.txt')
    with open(log_file_path, 'a') as f:
        f.write(f"Received webhook payload: {basic_info}\n")
    return 'Webhook received successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8027)



'''
timestamp 
ref
user
commit id (last)

'''
from flask import Flask, request

app = Flask(__name__)

def extract_basic_info(data):
    repo_name = data.get('repository', {}).get('name', 'Unknown Repo')
    pusher_name = data.get('pusher', {}).get('name', 'Unknown Pusher')
    branch_ref = data.get('ref', 'Unknown Branch')
    return f"Repo: {repo_name}, Pusher: {pusher_name}, Branch: {branch_ref}"

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    data = request.json
    basic_info = extract_basic_info(data)
    # Write basic information of the received JSON payload to log.txt
    with open('log.txt', 'a') as f:
        f.write(f"Received webhook payload: {basic_info}\n")
    return 'Webhook received successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8027)

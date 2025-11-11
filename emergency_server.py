from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client
import os

app = Flask(__name__)
CORS(app)

# Twilio configuration
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE = os.getenv('TWILIO_PHONE', '+17163210851')
RESCUE_TEAM_PHONE = os.getenv('RESCUE_TEAM_PHONE', '+918889441539')

def trigger_emergency_call(location=""):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        
        twiml_message = f"""
        <Response>
            <Say voice="alice" rate="slow">
                Emergency alert. This is an automated message from the emergency response system. 
                An emergency has been detected at {location}. 
                Immediate assistance is required. 
                Please respond as soon as possible. 
                Thank you.
            </Say>
        </Response>
        """
        
        call = client.calls.create(
            twiml=twiml_message,
            to=RESCUE_TEAM_PHONE,
            from_=TWILIO_PHONE
        )
        
        return call.sid
    except Exception as e:
        print(f"Failed to make emergency call: {e}")
        return None

@app.route('/emergency', methods=['POST'])
def handle_emergency():
    data = request.get_json()
    location = data.get('location', 'Unknown location')
    
    call_sid = trigger_emergency_call(location)
    
    if call_sid:
        return jsonify({'success': True, 'call_sid': call_sid})
    else:
        return jsonify({'success': False, 'error': 'Failed to initiate call'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import twilio from 'twilio';

dotenv.config();

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

const client = twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

app.post('/emergency', async (req, res) => {
  try {
    const { location } = req.body;
    
    const call = await client.calls.create({
      twiml: `<Response><Say>Emergency alert! Location: ${location}. Please respond immediately.</Say></Response>`,
      to: process.env.RESCUE_TEAM_PHONE,
      from: process.env.TWILIO_PHONE
    });

    console.log('Emergency call initiated:', call.sid);
    res.json({ success: true, callSid: call.sid });
  } catch (error) {
    console.error('Twilio error:', error);
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(port, () => {
  console.log(`🚨 Emergency server running on port ${port}`);
});

export default app;
# Install Satellite Detection Dependencies

Run these commands in the ResQAI directory:

```bash
cd d:\ResQ\ResQAI
npm install google-map-react
```

If you get any TypeScript errors, also install:

```bash
npm install @types/google-map-react
```

## Test the Integration

1. Start the development server:
```bash
npm run dev
```

2. Navigate to: http://localhost:5173/satellite

3. You should see the satellite detection page with:
   - NASA wildfire data
   - Global map with fire markers
   - Real-time tracking interface

## Features Added:
✅ Satellite detection page at `/satellite`
✅ Navigation menu item with satellite icon
✅ Integration with main dashboard layout
✅ NASA EONET wildfire data
✅ Google Maps with fire markers
✅ Sample data fallback
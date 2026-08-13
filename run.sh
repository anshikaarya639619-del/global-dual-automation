#!/bin/bash

echo "🔥 [GOD-MODE] Starting MrBeast Infinite Automation Empire..."

while true
do
    echo "⏰ [$(date)] Triggering Main Content Pipeline..."
    python3 main.py
    
    echo "📡 [$(date)] Triggering 20-Hour Live Stream Dispatcher..."
    python3 live_streamer.py
    
    echo "💤 Cycle complete. Standing by for next schedule interval..."
    sleep 3600
done

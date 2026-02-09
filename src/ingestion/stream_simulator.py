# src/ingestion/stream_simulator.py

import time
import pandas as pd

from src.ingestion.window_manager import RollingWindowManager
from src.utils.config import STREAM_SLEEP_SECONDS

class StreamSimulator:
    """
    Simulates real-time streaming from historical market data.
    """

    def __init__(self, csv_path: str):
        self.data = pd.read_csv(csv_path)
        self.data["timestamp"] = pd.to_datetime(self.data["timestamp"])
        self.window_manager = RollingWindowManager()
    def start(self):
        """
        Start emitting market events one by one.
        """
        for _, row in self.data.iterrows():
            event = {
                "ticker": row["ticker"],
                "timestamp": row["timestamp"],
                "open": row["open"],
                "high": row["high"],
                "low": row["low"],
                "close": row["close"],
                "volume": row["volume"],
            }

            self.window_manager.add_event(event["ticker"], event)

            print(
                f"Streamed {event['ticker']} @ {event['timestamp']} | "
                f"Window size: {len(self.window_manager.get_window(event['ticker']))}"
            )

            time.sleep(STREAM_SLEEP_SECONDS)

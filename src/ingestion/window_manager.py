# src/ingestion/window_manager.py

from collections import deque
from datetime import timedelta
import pandas as pd

from src.utils.config import ROLLING_WINDOW_MINUTES

class RollingWindowManager:
    """
    Maintains a rolling time window of market data per ticker.
    """

    def __init__(self):
        # Dictionary: ticker -> deque of events
        self.windows = {}
    def add_event(self, ticker: str, event: dict):
        """
        Add a new market event to the rolling window.
        """
        if ticker not in self.windows:
            self.windows[ticker] = deque()

        self.windows[ticker].append(event)
        self._remove_old_events(ticker)
    def _remove_old_events(self, ticker: str):
        """
        Remove events older than rolling window duration.
        """
        window = self.windows[ticker]
        if not window:
            return

        latest_time = window[-1]["timestamp"]
        cutoff_time = latest_time - timedelta(minutes=ROLLING_WINDOW_MINUTES)

        while window and window[0]["timestamp"] < cutoff_time:
            window.popleft()
    def get_window(self, ticker: str) -> pd.DataFrame:
        """
        Return the rolling window for a ticker as a DataFrame.
        """
        if ticker not in self.windows:
            return pd.DataFrame()

        return pd.DataFrame(list(self.windows[ticker]))

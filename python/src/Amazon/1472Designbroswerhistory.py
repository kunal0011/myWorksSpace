class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]  # Stack for the history of URLs
        self.current = 0  # Index for the current page in the history

    def visit(self, url: str) -> None:
        # When we visit a new page, all forward history is lost
        # Remove all forward history
        self.history = self.history[:self.current + 1]
        self.history.append(url)  # Add the new page
        self.current += 1  # Move to the new current page

    def back(self, steps: int) -> str:
        # Move back by steps, but ensure we don't go beyond index 0
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward by steps, but ensure we don't go beyond the latest page
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]

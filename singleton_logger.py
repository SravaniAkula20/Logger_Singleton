from datetime import datetime
import threading

from logger import Logger, LogLevel


class LoggerImpl(Logger):

    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls):
        # TODO:
        # Implement Singleton creation.
        # Consider thread safety while creating the instance.
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance= super().__new__(cls)
        return cls._instance

    def __init__(self):
        # TODO:
        # Initialize the logger only once.
        #
        # You will need fields for:
        # - log file path
        # - file object
        # - lock for log operations
        if hasattr(self,"_initialized"):
            return
        self.file= None
        self.file_path = None
        self._initialized = True

    @classmethod
    def get_instance(cls):
        # TODO:
        # Return the Singleton instance.
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls):
        # TODO:
        # Reset the Singleton instance.
        # Think about what should happen if a file is still open.
        if cls._instance is not None:
            cls._instance.close()
        cls._instance = None

    def set_log_file(self, file_path):
        # TODO:
        # Open the log file and store the file path.
        if self.file is not None:
            self.file.close()

        self.file = open(file_path,"a")
        self.file_path = file_path

    def log(self, level, message):
        # TODO:
        # 1. Check whether the logger has been initialized.
        # 2. Create a timestamp.
        # 3. Format the log entry.
        # 4. Write it to the file.
        # 5. Make the operation thread-safe.
        d = datetime.now()
        entry = f"{d},[{level.value}],{message},\n"
        self.file.write(entry)

    def get_log_file(self):
        # TODO:
        # Return the current log file path.
        return self.file_path

    def flush(self):
        # TODO:
        # Flush buffered log entries.
        self.file.flush()

    def close(self):
        # TODO:
        # Close the file resource.
        self.file.close()

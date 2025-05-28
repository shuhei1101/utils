class TestAppLogger:
    def test_各レベルのログを出力できること(self, app_logger):
        app_logger.debug("Debug message")
        app_logger.info("Info message")
        app_logger.warning("Warning message")
        app_logger.error("Error message")
        app_logger.critical("Critical message")

        # Check if the logs are written to the file
        with open(app_logger.log_file, 'r') as f:
            logs = f.read()
            assert "Debug message" in logs
            assert "Info message" in logs
            assert "Warning message" in logs
            assert "Error message" in logs
            assert "Critical message" in logs
            
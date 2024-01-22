import os, sys, time, re, logging
from datetime import datetime

from dirsync import sync


def main():
    source_folder_path = sys.argv[1]
    replica_folder_path = sys.argv[2]
    frequency = sys.argv[3]
    log_file_path = sys.argv[4]

    sync_logger = logging.getLogger(f"{log_file_path}\\syncLog.txt")
    sync_logger.setLevel(logging.INFO)
    sync_logger.addHandler(logging.FileHandler(f"{log_file_path}\\syncLog.txt"))
    sync_logger.addHandler(logging.StreamHandler(stream=sys.stdout))

    sync_logger.info(f"Syncing app started.")
    sync_logger.info(f"Source: {source_folder_path}")
    sync_logger.info(f"Replica:{replica_folder_path}")
    sync_logger.info(f"Log:{log_file_path}")
    sync_logger.info(f"Time: {datetime.now()}")
    sync_logger.info(f"Frequency: {frequency}\n")

    # check incoming params
    if error1 := not re.match(r"^[1-9][0-9]*$", frequency):
        sync_logger.error("Has to be a positive integer. Terminating the application.")
    if error2 := not os.path.exists(source_folder_path):
        sync_logger.error("Source folder path doesn't exist. Terminating the application.")
    if error3 := not os.path.exists(log_file_path):
        sync_logger.error("Log file path doesn't exist. Terminating the application.")
    # abort if errors
    if error1 or error2 or error3:
        return

    # continue
    sync_logger.info("Correct input.\n")
    while True:
        sync_logger.info("NEW SYNC")
        sync_logger.info(f"Syncing time: {datetime.now()}\n")

        sync(source_folder_path, replica_folder_path, 'sync', logger=sync_logger, purge=True, ctime=True, create=True)

        sync_logger.info(f"Folder synced at {datetime.now()}\n\n")
        time.sleep(int(frequency) * 60)

if __name__ == "__main__":
    main()

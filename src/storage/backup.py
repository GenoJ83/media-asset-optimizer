import shutil
def backup_original_file(src: str, backup_dir: str):
    os.makedirs(backup_dir, exist_ok=True)
    shutil.copy2(src, backup_dir)

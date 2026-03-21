from pathlib import Path


def validate_input(input_path, supported_extensions={".m4a"}):
    """
    This function does 3 things:
    1. Ensure the path exists
    2. Asses if input is a folder or a file
    3. Ensure the files in the path are in supported format
    """
    audio_path = Path(input_path)

    # 1. Ensure the path exists
    if not audio_path.exists():
        raise FileNotFoundError(f"File/folder not found: {input_path}")
    
    # 2. Assess if the input is a folder or a file
    is_file = True
    if audio_path.is_dir():
        is_file = False

    # 3. Ensure the files at the path are in supported foramt
    # In case of folder, this function checks if at least one file is in supported file format.
    if is_file:
        if audio_path.suffix not in supported_extensions:
            raise ValueError(f"Only files in these format are supported: {supported_extensions}")
        else:
            file_paths = [audio_path]
            
    else:
        file_paths = extract_supported_files(audio_path)
        if not file_paths:
            raise ValueError(f"The folder doesn't contain any file in the supported format: {supported_extensions}")
    
    return is_file, file_paths


def extract_supported_files(input_folder_path, supported_extensions={".m4a"}):
    supported_file_paths = set()
    
    if not input_folder_path.is_dir():
        return supported_file_paths
    
    list_of_files = input_folder_path.iterdir()
    for file in list_of_files:
        if file.suffix.lower() in supported_extensions:
            supported_file_paths.add(file)

    return supported_file_paths
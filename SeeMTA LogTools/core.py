def read_log_file(file_path):
    """
    opens log file from the desired path.
    Parameters:
    fileDirectory (str or list): the path to the desired file
    Returns:
    list:file content
    """
    if isinstance(file_path, str):
        try:
            file = open(file_path, "r", encoding="UTF-8")
            file_content = file.readlines()
            for i in range(len(file_content)):
                file_content[i] = file_content[i].replace("\n" , "")
            file.close()
            return file_content
        except:
            print("Hiba a fájl betöltésekor!")
            exit(11)
    elif isinstance(file_path, list):
        all_content = []
        for i in file_path:
            try:
                file = open(i, "r", encoding="UTF-8")
                file_content = file.readlines()
                for i in range(len(file_content)):
                    file_content[i] = file_content[i].replace("\n" , "")
                    all_content.append(file_content[i])
                file.close()
            except:
                print("Hiba a fájlok beolvasásakor!")
                exit(11)
        return all_content
    else:
        exit(10)
class Main:
    @staticmethod
    def openFile(file_path):
        """
        opens log file from the desired path.
        Parameters:
        fileDirectory (str, optional): the path to the desired file
        Returns:
        list:file content
        """
        file = open(file_path, "r", encoding="UTF-8")
        content = file.readlines()
        for i in range(len(content)):
            content[i] = content[i].replace("\n" , "")
        file.close()
        return content


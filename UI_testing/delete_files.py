import os

def delete_file(file_name):
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        try:
            if os.path.exists(file_path):
                confirm = input(f"Do you want to remove '{file_name}' file? (yes/no): ")
                if confirm.lower() == "yes":             
                    os.remove(file_path) 
                    print(f"'{file_name}' file with its content has been deleted.")
                elif confirm.lower() == "no":
                    print(f"'{file_name}' file hasn't been deleted.")

                else: 
                    print(f"'{file_name}' file hasn't been deleted, because of incorrect input.")

            else:
                print(f"'{file_name}' file doesn't exist.")
        except Exception as e:
            print(f"Error occured while deleting '{file_name}' file. Exception: {e}")

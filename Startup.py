from imports import *


class Startup:
    def add_to_startup(file_path=""):
        if not file_path:
            file_path = os.path.realpath(__file__)  # type: ignore
        file_name = os.path.basename(file_path)  # type: ignore
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_WRITE)  # type: ignore
            reg.SetValueEx(registry_key, file_name, 0, reg.REG_SZ, file_path)  # type: ignore
            reg.CloseKey(registry_key)  # type: ignore
            print(f"Added {file_name} to startup")
        except Exception as e:
            print(f"Failed to add to startup: {e}")

    def remove_from_startup(file_path=""):
        if not file_path:
            file_path = os.path.realpath(__file__)  # type: ignore
        file_name = os.path.basename(file_path)  # type: ignore
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_WRITE)  # type: ignore
            reg.DeleteValue(registry_key, file_name)  # type: ignore
            reg.CloseKey(registry_key)  # type: ignore
            print(f"Removed {file_name} from startup")
        except FileNotFoundError:
            print(f"{file_name} not found in startup")
        except Exception as e:
            print(f"Failed to remove from startup: {e}")

    def is_in_startup(file_path=""):
        if not file_path:
            file_path = os.path.realpath(__file__)  # type: ignore
        file_name = os.path.basename(file_path)  # type: ignore
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_READ)  # type: ignore
            value, reg_type = reg.QueryValueEx(registry_key, file_name)  # type: ignore
            reg.CloseKey(registry_key)  # type: ignore

            if value == file_path:
                return True
            else:
                print(
                    f"Registry value does not match the expected path: {value} != {file_path}"
                )
                return False
        except FileNotFoundError:
            print(f"Registry entry not found for: {file_name}")
            return False
        except Exception as e:
            print(f"Failed to check registry: {e}")
            return False


if __name__ == "__main__":
    # Pass the script path to the function
    Startup.add_to_startup("D:\college\Project\新建文件夹\StickyNotesMain.py")

    Startup.is_in_startup("D:\college\Project\新建文件夹\StickyNotesMain.py")

    # Pass the script name (or the name used to add the startup entry) to the function
    Startup.remove_from_startup("D:\college\Project\新建文件夹\StickyNotesMain.py")

    Startup.is_in_startup("D:\college\Project\新建文件夹\StickyNotesMain.py")

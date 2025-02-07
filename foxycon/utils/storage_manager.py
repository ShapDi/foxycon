import os
import json

class StorageManager:
    PATH_DIR = os.getcwd()

    @staticmethod
    def add_data_storage(group, data):
        with open("storage.json", "w+", encoding="utf-8") as file:
            save_data = json.load(file)
            data_group = save_data.get(group)
            if data_group is None:
                data_group = {group: data}
            else:
                data_group.update(data)
            save_data[group] = data_group
            json.dump(save_data, file, indent=4, ensure_ascii=False)
        return data

    @staticmethod
    def get_data_storage(group, name_data):
        with open("storage.json", "r+", encoding="utf-8") as file:
            save_data = json.load(file)
            data_group = save_data.get(group)
            if data_group is None:
                return None
            data_group.get(name_data)
        return data_group




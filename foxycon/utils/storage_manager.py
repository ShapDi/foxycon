import os
import json
from dataclasses import asdict

from foxycon.data_structures.balancer_type import BalancerType
from foxycon.utils.balancers import Balancer


class StorageManager:
    def __init__(self, path_file: str):
        self._path_file = path_file
        self._balancers: list[Balancer] = []

    def add_balancer(self, balancer:Balancer):
        self._balancers.append(balancer)

    def add_balance_object(self, balance_object: BalancerType):
        pass

    def get_balance_object(self):
        pass


class StorageManagerOld:
    PATH_FILE = "storage.json"

    @staticmethod
    def _load_storage():
        if not os.path.exists(StorageManager.PATH_FILE):
            return {}
        try:
            with open(StorageManager.PATH_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}

    @staticmethod
    def _save_storage(data):
        with open(StorageManager.PATH_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def add_data_storage(group, data):
        save_data = StorageManager._load_storage()

        if group not in save_data:
            save_data[group] = {}

        save_data[group][str(data.api_id)] = asdict(data)
        StorageManager._save_storage(save_data)
        return data

    @staticmethod
    def get_data_storage(group, api_id):
        save_data = StorageManager._load_storage()
        return save_data.get(group, {}).get(str(api_id))

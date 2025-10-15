import os
import json


class SignupLoginDataReader:
    @staticmethod
    def read_json(file_name):
        """
        Reads data from a JSON file located in the `data` folder.
        :param file_name: The name of the JSON file (e.g., 'test_data.json').
        :return: Parsed JSON data as a dictionary.
        """
        data_path = os.path.join(os.path.dirname(__file__), "../data", file_name)
        try:
            with open(data_path, "r") as file:
                return json.load(file)
        except FileNotFoundError :
            raise FileNotFoundError(f"Data file '{file_name}' not found in the 'data' folder.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file '{file_name}': {e}")
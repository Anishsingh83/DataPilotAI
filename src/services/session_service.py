from flask import session


class SessionService:

    @staticmethod
    def set_current_dataset(dataset_name, dataset_path):

        session["dataset_name"] = dataset_name
        session["dataset_path"] = dataset_path

    @staticmethod
    def get_current_dataset():

        return {
            "dataset_name": session.get("dataset_name"),
            "dataset_path": session.get("dataset_path")
        }

    @staticmethod
    def has_dataset():

        return "dataset_path" in session

    @staticmethod
    def clear_dataset():

        session.pop("dataset_name", None)
        session.pop("dataset_path", None)
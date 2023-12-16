import json


class Task:
    def __init__(self):
        self.text = ""
        self.checkbox = False
        self.id = 0

    def reassign_id(self, data):
        i = 1
        for d in data["tasks"]:
            d["id"] = i
            i += 1

    def add_tasks(self, t):
        self.text = t
        task_dict = {"text": self.text, "checkbox": False}
        with open("task.json") as file:
            data = json.load(file)
        data["tasks"].append(task_dict)
        self.reassign_id(data)
        with open("task.json", "w") as file:
            json.dump(data, file, indent=2)
        file.close()

    def delete_tasks(self, id):
        with open("task.json", "r") as file:
            data = json.load(file)
        for val in data["tasks"]:
            if val["id"] == id:
                del data["tasks"][id - 1]
        self.reassign_id(data)
        with open("task.json", "w") as f:
            json.dump(data, f, indent=2)
        file.close()

    def view(self):
        self.task_list = []
        with open("task.json", "r") as file:
            data = json.load(file)
        for val in data["tasks"]:
            if val["checkbox"] == False:
                val["checkbox"] = "Not done"
            else:
                val["checkbox"] = "done"
            self.task_list.append(str(val["id"]) + " ." + val["text"] + "    |" + str(val["checkbox"]))
        file.close()

    def clear_all(self):
        with open("task.json", "r") as file:
            data = json.load(file)
        data["tasks"].clear()
        with open("task.json", "w") as f:
            json.dump(data, f, indent=2)
        file.close()

    def update_task(self, id):
        with open("task.json", "r") as file:
            data = json.load(file)
        if data["tasks"][id - 1]["checkbox"]:
            data["tasks"][id - 1]["checkbox"] = False
        else:
            data["tasks"][id - 1]["checkbox"] = True
        with open("task.json", "w") as file:
            json.dump(data, file, indent=2)
        file.close()

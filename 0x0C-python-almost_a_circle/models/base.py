#!/usr/bin/python3
"""
Defines a Base module.
"""
import json


class Base:
    """Initialize Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dict respersentaion.

        Returns:
            (str): Json represantation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.

        Args:
            cls: class
            list_objs (list): is list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        li = []
        if list_objs is not None:
            for i in list_objs:
                li.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """Represent json string"""
        if json_string is None or json_string is "":
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file_csv: loads froom csv file and create objects
        """
        filename = cls.__name__ + ".csv"
        inst = []
        d = {}
        if os.path.exists(filename) is True:
            with open(filename) as fd:
                result = csv.reader(fd, delimiter=',')
                for row in result:
                    a = []
                    for elem in row:
                        a.append(int(elem))

                    if cls.__name__ == "Rectangle":
                        new = ['id', 'width', 'height', 'x', 'y']
                        for i in range(len(a)):
                            d[new[i]] = a[i]
                        inst.append(cls.create(**d))
                    if cls.__name__ == "Square":
                        new = ['id', 'size', 'x', 'y']
                        for i in range(len(a)):
                            d[new[i]] = a[i]
                        inst.append(cls.create(**d))
            return(inst)
        else:
            return(result)

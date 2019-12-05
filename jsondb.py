import json
import os
DIR = os.path.dirname(os.path.realpath(__file__))+ os.path.sep

class jsondb:

    def __init__(self, name):
        self.db = [] #the main var that stores all the data
        self.name = name #this var is used to set the saved file's name
        self.load()

    def load(self): #used to load a database from a file
        if not os.path.isfile(DIR+ self.name+ ".jsondb"):
            return False
        dbfile = open(DIR+ self.name+ ".jsondb", "r")
        self.db = json.load(dbfile)
        return True

    def open_file_writemode(self): #used to open database file in write mode
        self.file = open(DIR+ self.name+ ".jsondb", "w")

    def save(self): #used to write the database into a file
        self.open_file_writemode()
        json.dump(self.db, self.file)
        self.file.close()
        
    def register(self, obj): #used to add a new object to the db (given object must be an instance of dict object)
        if not type(obj) == dict:
            return False

        self.db.append(obj)
        self.save()
        return True

    def search(self, param, requested_value): #used to return all items that has the same specified value and param 
        results = []
        for element in self.db:
            if param in element:
                if element[param] == requested_value:
                    results.append(element)

        return results

    def search_param(self, param): #used to return all items that has a specified param
        results = []
        for element in self.db:
            if param in element:
                results.append(element)

        return results

    def remove(self, item): #used to remove a single item from db
        if item in self.db:
            self.db.remove(item)
            self.save()
            return True

        else:
            return False

    def remove_all(self, item): #used to remove an item and its copies from db
        if item in self.db:
            for i in range(self.db.count(item)):
                self.db.remove(item)

            self.save()
            return True

        else:
            return False

    def mass_remove(self, given_list): #used to remove all items specified in a list from db
        for item in given_list:
            if item in self.db:
                self.db.remove(item)

        self.save()

    def mass_remove_all(self, given_list): #used to remove all items and their copies specified in a list from db
        for item in given_list:
            if item in self.db:
                for i in range(self.db.count(item)):
                    self.db.remove(item)

        self.save()
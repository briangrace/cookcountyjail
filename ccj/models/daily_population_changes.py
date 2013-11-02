#
# Model for sumarized Daily Population Changes
#

from json import dumps
from os.path import isfile
import csv


class DailyPopulationChanges:

    def __init__(self, path):
        self._path = path
        self._column_names = ['date', 'booked_males_as']
        self._initialize_file()

    def clear(self):
        """ Write our fieldnames in CSV format to the file we're wrapping,
            creating the file if it doesn't already exist. """
        # lock here
        try:
            with open(self._path, 'w') as f:
                w = csv.writer(f)
                w.writerow(self._column_names)
        except IOError:
            raise Exception("There's something wrong with the path "
                            "configured for our file's creation on your system, "
                            "at '{0}'.".format(self._path))

    def _initialize_file(self):
        """ Make sure the file exists. If it doesn't, first create it,
            then initialize it with our fieldnames in CSV format. """
        # make sure the file exists
        if not isfile(self._path):
            # If not, create a file and
            # put an empty list inside it
            self.clear()

    def store(self, entry):
        """
        Append an entry to our file. Expects a dict object.

        If a non-dict-like object is stored using this method,
        we won't know until we hit the formatting methods,
        while querying it, which is confusing.
        """
        assert isinstance(entry, dict)
        # lock here
        with open(self._path, 'a') as f:
            w = csv.writer(f)
            w.writerow(entry.values())

    def query(self):
        """
        Return the data stored in our file as Python objects.
        """
        #lock here
        with open(self._path) as f:
            rows = csv.DictReader(f)
            query_results = [row for row in rows]
            return query_results

    def to_json(self):
        """
        Return the data stored in our file as JSON.
        """
        query_results = self.query()
        json_value = dumps(query_results)
        return json_value

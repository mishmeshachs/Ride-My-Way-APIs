
"""
declaration of global variables.
"""
rides = []


class RidersModel:

    def __init__(self, ref_no, date,price,source, destination):
        

        self.ride_id = self.generate_id(rides)
        self.ref_no = ref_no
        self.date = date
        self.price= price
        self.source= source
        self.destination = destination

    def create_ride(self):
      
        ride = {
            "id": self.ride_id,
            "ref_no": self.ref_no,
            "date": self.date,
	    "price": self.price,
            "source":self.source,
            "destination": self.destination
        }

        rides.append(ride)

        return ride

    @staticmethod
    def get_ride(ride_id):
        """
                returns a single ride
        """

        for ride in rides:
            if ride.get('id') == ride_id:
                return ride
            continue

        return "Error on selection try again"

    @staticmethod
    def get_rides():
        """
                all available rides
        """
        if rides:
            return rides
        return "selected ride not found"

    @staticmethod
    def delete_ride(ride_id):
        for count, ride in enumerate(rides):
            if ride.get("id") == ride_id:
                rides.pop(count)
                return rides
        return "Ride not Found"

    @staticmethod
    def generate_id(_list):
        """
                list of selected IDs
        """
        if _list:
            return _list[-1].get("id") + 1
        return 1

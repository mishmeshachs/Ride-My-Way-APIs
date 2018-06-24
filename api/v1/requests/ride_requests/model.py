from api.v1.rides.model import RidersModel

"""
     Riders Variables on 
"""
ride_requests = []


class RideRequestModel:

    def __init__(self, user_id, ride_id):
       
        self.request_id = RideModel.generate_id(ride_requests)
        self.user_id = user_id
        self.ride_id = ride_id
        self.status = "pending"

    def create_request(self):

       

        request = {

            "id": self.request_id,
            "user_id": int(self.user_id),
            "ride_id": int(self.ride_id),
            "status": "pending"
        }
        ride_requests.append(request)

        return request

    @staticmethod
    def get_request(request_id):

        """
              This method returns a particular ride of the id given to it from the list of available rides
        """

        global ride_requests

        for request in ride_requests:
            if request.get("id") == int(request_id):
                return request
            continue
        return "Ride request not found"

    @staticmethod
    def get_requests():

        """
             This method returns all requests created in our ride_requests list declared above
        """

        if ride_requests:
            return ride_requests
        else:
            return "No ride requests found"


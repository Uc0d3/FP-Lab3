

class Validator:

    @staticmethod
    def validate_rating(rating):
        try:
            rating = float(rating)
            if (rating < 0):
                raise Exception("Rating can not be negative")
            if (rating < 0 or rating > 10):
                raise Exception("rating should be > 0 and < 10")
        except ValueError:
            raise Exception("Rating is not a valid number")

    @staticmethod
    def validate_year(year):
        try:
            year = int(year)
            if (year < 0):
                raise Exception("Year can not be negative")
        except ValueError:
            raise Exception("Year is not a valid integer")

    @staticmethod
    def validate_price(price):
        try:
            price = float(price)
            if (price < 0):
                raise Exception("Price can not be negative")
        except ValueError:
            raise Exception("Price is not a valid number")

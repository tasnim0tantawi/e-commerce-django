class Cart():
    def __init__(self, request):
        self.session = request.session  # to make the session available in the whole class
        cart = self.session.get('session_key')  # our returning users will get their existing session_key

        # if the user is new, we will create a new session for him
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # The cart will be empty if the user is new, and it will be filled with products if the user is returning
        self.cart = cart



class SelectionValidation:

    """This class provides function to detect user's input."""

    # Count the times of wrong input, pop up menu again when > 5
    invalid_input_counter = 0

    def __init__(self, selection_dict, menu_message, welcome_message):
        self.selection_dict = selection_dict
        self.menu_message = menu_message
        print(self.menu_message)
        self.welcome_message = welcome_message
        self.user_input = input(welcome_message)

    def validation(self):

        while self.user_input not in self.selection_dict:
            if self.invalid_input_counter >= 4:
                print(self.menu_message)
                self.invalid_input_counter = 0
                self.user_input = input(self.welcome_message)
                continue
            self.user_input = input("Invalid selection, please select again:")
            self.invalid_input_counter += 1

        return self.user_input

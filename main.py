import random
import string

class PasswordModes:
    """Manages different password complexity modes."""
    def __init__(self):
        self.modes = {
            "mode_1": {
                'length': 16,
                'upper': True,
                'lower': True,
                'number': True,
                'punc': True
            },
            "mode_2": {
                'length': 20,
                'upper': False,
                'lower': True,
                'number': True,
                'punc': False
            },
        }

    def get_mode_details(self, mode):
        """Retrieves and returns configuration for a specified mode."""
        if mode not in self.modes:
            raise ValueError(f"Invalid mode: {mode}")
        return self.modes[mode]

def generate_password(mode_details):
    """Generates a password based on provided mode details."""
    length = mode_details['length']
    upper = mode_details['upper']
    lower = mode_details['lower']
    number = mode_details['number']
    punc = mode_details['punc']

    print(length,upper,lower,number,punc)

    char_sets = (string.ascii_uppercase * upper + string.ascii_lowercase * lower +
                 string.digits * number + string.punctuation * punc)
    
    if not char_sets:
        raise ValueError("Password must include at least one character type.")

    return ''.join(random.choice(char_sets) for _ in range(length))

if __name__ == '__main__':
    pm = PasswordModes()
    mode_details = pm.get_mode_details("mode_1")  # Ensuring correct mode is referenced
    password = generate_password(mode_details)
    print(password)

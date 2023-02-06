from re import findall

# Defining custom messages inside the class, so we can handle the errors without stopping the program.
# User still sees additional information as intended


class NameTooShortError(Exception):
    """
    Raises an error if the username in current e-mail is shorter than
    the value stored in constant MIN_LENGTH
    """
    def __str__(self):
        return f"Name must be more than {MIN_LENGTH} characters"


class MustContainAtSymbolError(Exception):
    """ Raises an error if the current e-mail is missing '@' symbol. """

    def __str__(self):
        return f"Email must contain '@' symbol"


class InvalidDomainError(Exception):
    """ Raises an error if the domain in current e-mail is not stored in the list 'valid_domains'. """

    def __str__(self):
        return f"Domain must be one of the following: {', '.join(valid_domains)}"


class ForbiddenSymbolsInNameError(Exception):
    """
    Raises an error if the username in current e-mail is containing symbols different than
    small or capital letters, numbers, dots, hyphens and underscores
    """
    def __str__(self):
        return f"Username must contain only small or capital letters,numbers, dots, hyphens and underscores."


class MissingPartOfTheDomainError(Exception):
    """ Raises an error if part of the domain is missing e.g. example_email@.com """
    def __str__(self):
        return f"Part of your domain is missing.Please consider inserting it" \
               f" -> @<<MISSING PART>>{email[email.index('@') + 1:]}"


class ForbiddenStringsInEmailError(Exception):
    """ Raises an error if the e-mail contains any substring that is stored in the list 'forbidden_strings'. """
    def __str__(self):
        return f"E-mail contains a forbidden word! -> {BLACK + BLACK_BACKGROUND + banned_word + RESET}"


# packing all errors into a tuple for easier access in the except statement
errors_to_be_handled = (
    MustContainAtSymbolError,
    InvalidDomainError,
    NameTooShortError,
    ForbiddenSymbolsInNameError,
    MissingPartOfTheDomainError,
    ForbiddenStringsInEmailError,
)
# setting requirements for our validator
MIN_LENGTH = 4
valid_domains = [".com", ".bg", ".org", ".net"]
forbidden_strings = ["hacker", "offender", "invalid.email", "cheater", "shenanegans", "shnookerdookies"]
pattern_username = r"[\w\.\-]+"

# colors used in ForbiddenStringsInEmailError for censoring the forbidden word
# you can still read it on the console by selecting it
# you for sure did not see and/or copy it from row 64
BLACK = '\033[30m'
RESET = '\033[0m'
BLACK_BACKGROUND = '\033[40m'


email = input("Enter an e-mail for validation or 'End' to exit: ")

while email != "End":
    # if we remove the try-except block and use only the conditional statements
    # test outputs still work as shown in the exercise document
    try:
        if "@" not in email:
            raise MustContainAtSymbolError

        if len(email.split("@")[0]) <= MIN_LENGTH:
            raise NameTooShortError

        if "." + email.split(".")[-1] not in valid_domains:
            raise InvalidDomainError()

        if findall(pattern_username, email)[0] != email.split("@")[0]:
            raise ForbiddenSymbolsInNameError

        if "@." in email:
            raise MissingPartOfTheDomainError

        for banned_word in forbidden_strings:
            if banned_word in email.lower():
                raise ForbiddenStringsInEmailError

    except errors_to_be_handled as error:
        print("An error has occurred: ", error)
    else:
        print("E-mail is valid!")

    email = input("Enter an e-mail for validation or 'End' to exit: ")

else:
    print("Thank you for your time and effort. Keep up the good work!")

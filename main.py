from api import fetcher
from data import aggregate

def main_wrapper():
    # Attribute are a thing
    print("This is the start of our tutorial")
    # fetcher.states_accessor()
    fetcher.states_accessor()
    fetcher.tracks_accessor()
    print("this is the end of our python tutorial")


if __name__ == "__main__":
    main_wrapper()
    # what is going on?

    # setup gitignore and pull template

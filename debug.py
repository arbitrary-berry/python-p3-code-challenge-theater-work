import ipdb

from lib.audition import Audition
from lib.role import Role


hamlet = Role("Hamlet")
ophelia = Role("Ophelia")

leo = Audition(hamlet, "Leo", "Malibu, Dr.", "708225999907")
anna = Audition(hamlet, "Anna", "Rohnert Park", "7042232929")
tony = Audition(hamlet, "Tony", "Silver Lake", "36959920002")


ipdb.set_trace()

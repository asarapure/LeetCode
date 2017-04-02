def no_duplicates(str_):
    print("testing string:-", str_)
    return len(str_) == len(set(str_))

no_duplicates("amzing")


# Another method.

print("\n2nd approach")
def no_duplicates_no_structures(str_):
    """ Now without using additional data structures """
    for letter in str_:
        if str_.count(letter) > 1:
            print(str_.count(letter))
            return False
    return True

print(no_duplicates_no_structures("yolaw"))
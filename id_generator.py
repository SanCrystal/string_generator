"""
** A property of arcnet technologies : feel free to make use of this code
    in any of your projects that requires it.
** Generate a Unique 24 string character for IDs matching.
"""
import errno,json,logging as logger,string,random
# create generator function
def generate_ids(length):
    """
        ** Generates random string char of a given length. In format of a dictionary 
    """
    ids = string.ascii_letters + string.digits
    return ("".join(random.choice(ids) for i in range(length)))

# Number of ids to be generated.
def number_of_ids_to_generate(length_of_char,number_to_generate):
    ids = [generate_ids(length_of_char) for i in range(number_to_generate) ]
    return({ f"ID_NO-{ids.index(ids[i]) + 1}": ids[i] for i in range(len(ids))})


#check duplicates 
def contains_duplicates(obj):
    """
        ** Checks for duplicated IDS and returns true if none and false if there is a duplicate
    """
    return(len(list(set([i for i in obj.values()]))) == len([i for i in obj.keys()]))

#write to file
def writer(file,Id_length,number_to_generate):
    """
        ** Writes to file in a json format, throws an error if there is a duplicated id generated
        ** Gives valid feedback to user.
    """
    try:
        data = number_of_ids_to_generate(Id_length,number_to_generate)
        # assert that there is no duplicate
        assert contains_duplicates(data), "Contains duplicate IDs. Regenerate data sets and try again"
        with open(file,"w") as f:
                f.write(json.dumps(data))
                print("file successfully written")
               
    except AssertionError as error_message:
        print(error_message)
    except OSError as error_os:
        if error_os.errno == errno.ENOENT:
            logger.error("File not found")
        elif error_os.errno == errno.EACCES:
            logger.error("Permision Denied: Ensure you have access rights to this file")
        else:
            logger.error("Unexpected error occured!")


#Write to file number of IDs needed with the length of string char needed.
writer("arcnet_ids.json",24,1000)


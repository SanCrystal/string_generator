"""
** A property of arcnet technologies : feel free to make use of this code
    in any of your projects that requires it.
** Generate a Unique 24 string character for IDs matching.
"""
import errno,json,logging as logger,string,random
import loopmap
# create generator function
def generate_ids(id_format, sep,length):
    
    """
        ** functions Generates random string char of a given length. In format of a dictionary 
    """
    def joinstring(str):
        return ("".join(random.choice(str) for i in range(length)))
    def l_only(sep):
        ids = string.ascii_letters 
        return loopmap.n_separator(joinstring(ids),sep)
    def n_only(sep):
        ids = string.digits 
        return loopmap.n_separator(joinstring(ids),sep)
    def nl_only(sep):
        ids = string.ascii_letters + string.digits
        return loopmap.n_separator(joinstring(ids),sep)
    def nls_only(sep):
        ids = string.ascii_letters + string.digits +string.punctuation
        return loopmap.n_separator(joinstring(ids),sep)
    collections = {"l_only":l_only,"n_only":n_only,"nl_only":nl_only,"nls_only":nls_only}


    if (len(id_format) > 0):
        return collections[id_format](int(sep) if sep !="" else None) #converts seperator string values to integer or none if empty

# Number of ids to be generated.
def number_of_ids_to_generate(id_format,length_of_char,number_to_generate):
    container,mapped=[],[]
    def genreturn_f(_type,sep):
        
        try:
            ids = [generate_ids(_type ,sep,length_of_char)  for i in range(number_to_generate) ]
             
            # ** Checks for duplicated IDS and returns true if none and false if there is a duplicate
            assert len(ids) == len(set(ids)) , "Generated IDs must be Unique"
            return(ids)
        except AssertionError as msg:
            print (msg)
    def logic  (format):
        return format[elements].split(" ")[1] if len(format[elements].split(" "))>1 else ""
    for elements in range(len(id_format)):    
        if (id_format[elements].split(" ")[0] == "l_only"):
            sep = logic(id_format)
            container.append(genreturn_f(id_format[elements].split(" ")[0],sep))
        elif (id_format[elements].split(" ")[0] == "n_only"):
            sep = logic(id_format)
            container.append(genreturn_f(id_format[elements].split(" ")[0],sep))
        elif (id_format[elements].split(" ")[0] == "nl_only"):
            sep = logic(id_format)
            container.append(genreturn_f(id_format[elements].split(" ")[0],sep))
        elif (id_format[elements].split(" ")[0] == "nls_only"):
            sep = logic(id_format)
            container.append(genreturn_f(id_format[elements].split(" ")[0],sep))
    # loop through container and map elements
  

    if len(container) == 1:
        loopmap.loop_one(container,mapped)
    elif len(container) == 2:
        loopmap.loop_two(container,mapped)
    elif len(container) == 3:
        loopmap.loop_three(container,mapped)
    elif len(container) == 4:
        loopmap.loop_four(container,mapped)
    
    return({ f"ID_NO-{mapped.index(mapped[i]) + 1}": mapped[i] for i in range(len(mapped))})
  
#write to file
def writer(file,id_format,Id_length,number_to_generate):
    """
        ** Writes to file in a json format, throws an error if there is a duplicated id generated
        ** Gives valid feedback to user.
    """
    try:
        # validate the input values 
        func = ["l_only","n_only","nl_only","nls_only"] # valid functions
        for i in range(len(id_format)):
            sep = id_format[i].split(" ")[1] if len(id_format[i].split(" "))>1 else 0
            if (len(id_format[i].split(" "))>1):
                # check if sep is empty string
                sep = sep if sep != "" else 0
            assert (id_format[i].split(" ")[0] in func and (isinstance(int(sep),int)) or sep == None) ,"Incorrect data : inputs , Ensure You input valid data type and integer separator values separated with space"
        data = number_of_ids_to_generate(id_format,Id_length,number_to_generate)
        assert len(data.keys()) >0, "Error, There is no ID(s) generated: please try again."

        # write values to file
        with open(file,"w") as f:
                f.write(json.dumps(data))
                print("file successfully written")
                     
    except AssertionError as error_message:
        print(error_message)
    except ValueError as error_message:
        print("Only integer values are required for separators!:: ",error_message)
    except OSError as error_os:
        if error_os.errno == errno.ENOENT:
            logger.error("File not found")
        elif error_os.errno == errno.EACCES:
            logger.error("Permision Denied: Ensure you have access rights to this file")
        else:
            logger.error("Unexpected error occured!")


#Write to file number of IDs needed with the length of string char needed.
# writer("arcnet_ids.json",["l_only","n_only 4"],24,1000)

# write to other file formats (convert to other file formats)
def write_to_other_file(from_file,to_file):
    try:
        with open(from_file,"r") as file_r:
            data = file_r.read()
        #write to other file
        with open(to_file,"w") as file_w:
            write_data = file_w.write(data)
    
    except OSError as error_os:
        if error_os.errno == errno.ENOENT:
            logger.error("File not found")
        elif error_os.errno == errno.EACCES:
            logger.error("Permision Denied: Ensure you have access rights to this file")
        else:
            logger.error("Unexpected error occured!")

write_to_other_file("arcnet_ids.txt","arcnet_ids.json")
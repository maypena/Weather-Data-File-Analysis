# May Pena
# This program reads weather data from a text file,
# processes the data, and outputs the answers to:
# coldest temperature recorded,
# warmest temperature recorded,
# and the 5 sunniest months and years.


def getInput():
    # =========================================================
    #  Get input from the user
    # =========================================================
    fileName = input( "File name: " )
    while True:
        try:
            text = open( fileName, "r" ).read()
            return text
        except:
            print( "Invalid file name.  Reenter" )
        fileName = input( "File name: " )
    return text

def coldest( text ):
    # =========================================================
    #  Year or years of the coldest temperature recorded
    # =========================================================
    print( "\n\n=== Coldest temperature recorded ===" )
    
    # prepare 2 empty lists
    list1 = []
    list2 = []

    # split the text into lines...
    lines = text.split( "\n" )
    
    for line in lines:
        
        # take out extra space
        line = line.strip()
        
        # take only empty lines
        if len( line )  != 0:
            
            # take only lines that start with a year
            if line[0] == '1' or line[0] == '2':
                
                # disregard asterisks
                line = line.replace( '*', '' )
                
                # disregard provisional
                line = line.replace( 'Provisional', '' )
                
                # split each line into words
                fields = line.split()
                
                # create a tuple with min temperarure,
                # month, and year
                try:
                    year  = fields[0]
                    month = fields[1]
                    tmin  = float( fields[3] )
                except ValueError: # disregard "---"
                    continue
                tuplex  = ( tmin, month, year )
                
                # add tupple to list
                list1.append( tuplex )
                
    # loop over. Sort it by lowest temp
    list1.sort()
    
    # put all of matching lowest temps in a list with their year
    lowest = list1[0][0]
    for tuplex in list1:
        if tuplex[0] == lowest:
            list2.append( tuplex[2] )
            list2.append( tuplex[1] )
            
    # print lowest temps in format
    print( "Temp, Year, Month" )
    print( str(lowest) + ",", ', '.join( list2) )


def warmest( text ):
    # =========================================================
    #   Year or years of the warmest temperature recorded
    # =========================================================
    print( "\n\n=== Warmest temperature recorded ===" )

    # prepare 2 empty lists
    list1  = []
    list2  = []

    # split the text into lines...
    lines = text.split( "\n" )

    for line in lines:
        
        # take out extra space
        line = line.strip()

        # take only empty lines
        if len( line )  != 0:
    
            # take only lines that start with a year
            if line[0] == '1' or line[0] == '2':
                
                # disregard asterisks
                line = line.replace( '*', '' )
                
                # disregard provisional
                line = line.replace( 'Provisional', '' )
                
                # split each line into words
                fields = line.split()
                
                # create a tuple with min temperarure,
                # month, and year
                try:
                    year  = fields[0]
                    month = fields[1]
                    tmax  = float( fields[2] )
                except ValueError: # disregard "---"
                    continue
                tuplex  = ( tmax, month, year)

                # add tupple to list
                list1.append( tuplex )
       
    # loop over. Sort it by highest temp
    list1.sort()
    list1.reverse()

    # put all of matching lowest temps in a list with their year
    maxTemp = list1[0][0]
    for tuplex in list1:
        if tuplex[0] == maxTemp:
            list2.append( tuplex[2] )
            list2.append( tuplex[1] )
            
    # print lowest temps in format
    print( "Temp, Year, Month" )
    print( str( maxTemp ) + ",", ', '.join( list2) )

def sunniest( text ):
    # =========================================================
    #    5 Sunniest months and years 
    # =========================================================
    print( "\n\n=== 5 Sunniest months and years ===" )
    
    # prepare 2 empty lists
    list1  = []
    list2 = []
    
    # split the text into lines...
    lines = text.split( "\n" )

    for line in lines:
        
        # take out extra space
        line = line.strip()
        
        # take only empty lines
        if len( line )  != 0:
            
            # take only lines that start with a year
            if line[0] == '1' or line[0] == '2':
                
                # disregard asterisks
                line = line.replace( '*', '' )
                
                # disregard provisional
                line = line.replace( 'Provisional', '' )
                
                # split each line into words
                fields = line.split()
                
                # create a tuple with min temperarure,
                # month, and year
                try:
                    year  = fields[0]
                    month = fields[1]
                    sun   = float( fields[6] )
                except ValueError: # disregard "---"
                    continue
                tuplex  = ( sun, year, month)

                # add tupple to list
                list1.append( tuplex )
       
    # loop over. Sort it by highest sun duration
    list1.sort()
    list1.reverse()

    # put 5 highest in a list
    count = 0
    for tuplex in list1:
        if count != 5:
            list2.append( str( tuplex[0] ) )
            list2.append( tuplex[1] )
            list2.append( tuplex[2] )
            count += 1
    # print 5 temps in format
    print( "Temp, Year, Month" )
    print( ', '.join( list2) )     


def main():
    text = getInput( )
    coldest ( text )
    warmest ( text )
    sunniest( text )

main()

lengthUnits = ('mm', 'milimetre', 'milimetres', 'milimeter', 'milimeters',
               'cm', 'centimetre', 'centimetres', 'centimeter', 'centimeters',
               'm', 'metre,', 'metres', 'meter', 'meters',
               'km', 'kilometre', '', 'kilometer', 'kilometers',
               'in', 'inch', 'inches', 'inches',
               'ft', 'foot', 'feet',
               'yd', 'yard', 'yards',
               'mi', 'mile', 'miles',
               'nmi', 'nautical mile', 'nautical miles')

speedUnits = ('ms', 'm/s',  'metres per second', 'meters per second',
              'fts', 'fps,' 'ft/s', 'f/s', 'feet per second',
              'ftm', 'ftm', 'ft/min', 'ft/m', 'feet per minute',
              'mph', 'mi/h', 'miles per hour', 'miles an hour',
              'ypm', 'yards/min', 'yards/m', 'yards per minute', 'y/m',
              'kmh', 'km/h', 'km per hour', 'kilometres per hour',
              'kn', 'knots')

timeUnits = ('nanosecond', 'nanoseconds','nanno', 'nannos', 'ns',
             'microsecond', 'microseconds', 'micro', 'micros', 'us', 'μs',
             'millisecond', 'milliseconds', 'milli', 'millis' 'ms',
             'second', 'seconds', 'sec', 'secs','s',
             'minute', 'minutes', 'min', 'mins', 'm',
             'hour', 'hours', 'hr', 'hrs', 'h',
             'day', 'days', 'd',
             'week', 'weeks', 'wk', 'wks', 'w',
             'month', 'months', 'mth', 'mths',
             'year', 'years', 'yr', 'yrs', 'y')

#Convert from m to a unit
lengthConversions = {'mm' : 1000, 'cm' : 100, 'm' : 1, 'km': 0.001, 'in' : 39.3701,
                     'ft' :  3.28084, 'yd' : 1.09361, 'mi': 0.000621371, 'nmi' : 0.000539957 }

speedConversions = {'ms' : 1, 'mph': 2.23694, 'kmh' : 3.6000059687997, 'kn' : 1.94384,
                   'fts': 3.28084, 'ftm': 196.85, 'ypm' : 65.6168}
timeConversions = {'min' : 1, 'hour': 0.0166667,  'day' :0.000694444, 'week': 0.000099206, 'month' : 0.000022831}
timeConversions['min'] = 1;
timeConversions['s'] = timeConversions['min'] * 60;
timeConversions['ms'] = timeConversions['s'] * 1000;
timeConversions['us'] = timeConversions['ms'] * 1000;
timeConversions['ns'] = timeConversions['us'] * 1000;
timeConversions['year'] = timeConversions['day'] / 365;

print(timeConversions)
def menu():
    print ('\n1)Length\n2)Speed\n3)Time')
    
    conversion = input('\nPlease enter the conversion you would like to use from the list above: ')

    if conversion == 'length' or conversion == 'Length' or conversion == '1':
        length()
    elif conversion == 'speed' or conversion == 'Speed' or conversion == '2':
         speed()
    elif conversion == 'time' or conversion == 'Time' or conversion == '3':
        time()
    else :
        print('Sorry your input didnt match one from the list above. please try again')
        menu()

def getValue():
    while True:
        try:
            number = float(input('Please input the value you want to convert: '))
            if number == 0:
                print("Enter a non zero value");
            else:
                break;
        except ValueError:
            print("Enter an numerical input");
    return number;

def length():
    unit = ' ';
    while unit not in lengthUnits:
        unit = input('\nPlease enter the unit of length you would like to convert from \n(mm, cm, m, km, inch, ft, yd, mi, nmi): ')
        unit = unit.lower()
    value = 0;
    value = getValue();
    
    if unit in ('mm', 'milimetre', 'milimetres', 'milimeter', 'milimeters'):
        convertLength(value, 'mm');
    elif unit in ('cm', 'centimetre', 'centimetres', 'centimeter', 'centimeters'):
        convertLength(value, 'cm');
    elif unit in ('m', 'metre,', 'metres', 'meter', 'meters'):
        convertLength(value, 'm');
    elif unit in ('km', 'kilometre', 'kilometres', 'kilometer', 'kilometers'):
        convertLength(value, 'km');
    elif unit in ('in', 'inch', 'inches', 'inches'):
        convertLength(value, 'in');
    elif unit in ('ft', 'foot', 'feet'):
        convertLength(value, 'ft');
    elif unit in ('yd', 'yard', 'yards'):
        convertLength(value, 'yd');
    elif unit in ('mi', 'mile', 'miles'):
        convertLength(value, 'mi');
    elif unit in ('nmi', 'nautical mile', 'nautical miles'):
        convertLength(value, 'nmi');
        
def convertLength(value, unit):
    valueInMeters = value / lengthConversions[unit]
    print("\n#####  Result  #####");
    print("Milimetres:  " + str(round(valueInMeters * lengthConversions['mm'],6)));
    print("Centimetres: " + str(round(valueInMeters * lengthConversions['cm'],6)));
    print("Metres:      " + str(round(valueInMeters * lengthConversions['m'],6)));
    print("Kilometre:   " + str(round(valueInMeters * lengthConversions['km'],6)));
    print("Inches:      " + str(round(valueInMeters * lengthConversions['in'],6)));
    print("Feets:       " + str(round(valueInMeters * lengthConversions['ft'],6)));
    print("Yards:       " + str(round(valueInMeters * lengthConversions['yd'],6)));
    print("Miles:       " + str(round(valueInMeters * lengthConversions['mi'],6)));
    print("nautical mile" + str(round(valueInMeters * lengthConversions['nmi'],6)));

def speed():
    unit = ' ';
    while unit not in speedUnits:
        unit = input('\nPlease enter the unit of speed you would like to convert from \n(m/s, ft/s , mph, kmh, knot): ')
        unit = unit.lower()
    value = 0;
    value = getValue();
    
    if unit in ('ms', 'm/s',  'metres per second', 'meters per second'):
        convertSpeed(value, 'ms');
    elif unit in ('fts', 'fps', 'ft/s', 'f/s', 'feet per second'):
        convertSpeed(value, 'fts');
    elif unit in ('ftm', 'ftm', 'ft/min', 'ft/m', 'feet per minute'):
        convertSpeed(value, 'ftm');
    elif unit in ('mph', 'mi/h', 'miles per hour', 'miles an hour'):
        convertSpeed(value, 'mph');
    elif unit in ('ypm', 'yards/min', 'yards/m', 'yards per minute', 'y/m'):
        convertSpeed(value, 'ypm');
    elif unit in ('kmh', 'km/h', 'km per hour', 'kilometres per hour'):
        convertSpeed(value, 'kmh');
    elif unit in ('kn', 'knots', 'knot'):
        convertSpeed(value, 'kn');

def convertSpeed(value, unit):
    valueInMS = value / speedConversions[unit]
    print("\n#####  Result  #####");
    print("Meters per second:  " + str(round(valueInMS * speedConversions['ms'],6)));
    print("Kilometres per hour:" + str(round(valueInMS * speedConversions['kmh'],6)));
    print("Miles per hour:     " + str(round(valueInMS * speedConversions['mph'],6)));
    print("knots:              " + str(round(valueInMS * speedConversions['kn'],6)));
    print("feet per minute:    " + str(round(valueInMS * speedConversions['ftm'],6)));
    print("yards per minute:   " + str(round(valueInMS * speedConversions['ypm'],6)));
    print("feet per second:    " + str(round(valueInMS * speedConversions['fts'],6)));

def time():
    unit = ' ';
    while unit not in timeUnits:
        unit = input('\nPlease enter the unit of time you would like to convert from \n(ms, second, hour, year etc.): ')
        unit = unit.lower()
    value = 0;
    value = getValue();
    
    if unit in ('nanosecond', 'nanoseconds','nanno', 'nannos', 'ns'):
        convertTime(value, 'ns');
    elif unit in ('microsecond', 'microseconds', 'micro', 'micros', 'us', 'μs'):
        convertTime(value, 'us');
    elif unit in ('millisecond', 'milliseconds', 'milli', 'millis' 'ms'):
        convertTime(value, 'ms');
    elif unit in ('second', 'seconds', 'sec', 'secs','s'):
        convertTime(value, 's');
    elif unit in ('minute', 'minutes', 'min', 'mins', 'm'):
        convertTime(value, 'min');
    elif unit in ('hour', 'hours', 'hr', 'hrs', 'h'):
        convertTime(value, 'hour');
    elif unit in ( 'day', 'days', 'd'):
        convertTime(value, 'day');
    elif unit in ('week', 'weeks', 'wk', 'wks', 'w'):
        convertTime(value, 'week');
    elif unit in ('month', 'months', 'mth', 'mths'):
        convertTime(value, 'month');
    elif unit in ('year', 'years', 'yr', 'yrs', 'y'):
        convertTime(value, 'year');


def convertTime(value, unit):
    valueInMins = value / timeConversions[unit]
    print("\n#####  Result  #####");
    print("Nanoseconds:   " + str(round(valueInMins * timeConversions['ns'],6)));
    print("Microseconds:  " + str(round(valueInMins * timeConversions['us'],6)));
    print("Milliseconds:  " + str(round(valueInMins * timeConversions['ms'],6)));
    print("Seconds:       " + str(round(valueInMins * timeConversions['s'],6)));
    print("Minutes:       " + str(round(valueInMins * timeConversions['min'],6)));
    print("Hour:          " + str(round(valueInMins * timeConversions['hour'],6)));
    print("Days:          " + str(round(valueInMins * timeConversions['day'],6)));
    print("Week:          " + str(round(valueInMins * timeConversions['week'],6)));
    print("Months(approx):" + str(round(valueInMins * timeConversions['month'],6)));
    print("Years:         " + str(round(valueInMins * timeConversions['year'],6)));
 
runAgain = True;
while(runAgain):
    menu();
    userInput = input("\nWoudld you like to run again? (y/n): ")
    if(userInput == 'y' or userInput == 'Y' or userInput == 'Yes' or userInput == 'YES' or userInput == 'yes'):
        runAgain = True;
    else:
        runAgain = False;
            

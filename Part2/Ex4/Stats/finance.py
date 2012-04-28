import datetime, optparse
import urllib2

def get_google_csv(ticker, date_start, date_end, unique_search=None):
    format="%b+%d+%Y"
    date_start = date_start.strftime(format)
    date_end = date_end.strftime(format)
    if unique_search is not None:
        search = unique_search
    else:
        search = ticker
    csvlink = "http://www.google.com/finance/historical?q=%s&startdate=%s&enddate=%s&output=csv"%(search, date_start, date_end)
    csv = ''
    try :
        csv = urllib2.urlopen(csvlink).read()
    except :
        print "trouble downloading CSV file; link used is"
        print "\t", csvlink
    return csv

def parse_csv(csv):
    csvlines = csv.split("\n")
    header = csvlines[0].split(',')
    for pos,entry in enumerate(header):
        if "Date" in entry: date_pos = pos
        if "Close" in entry: close_pos = pos
    
    lines = csvlines[1:]
    lines = (line.split(',') for line in lines)
    dt,format = datetime.datetime, "%d-%b-%y"
    data = ((dt.strptime(line[date_pos], format), float(line[close_pos])) for line in lines if len(line[date_pos])>0)
    return data


def script(ticker, start_date, end_date, unique_search):
    dt = datetime.datetime
    start_date = dt.strptime(start_date, "%m,%d,%Y")
    end_date = dt.strptime(end_date, "%m,%d,%Y")
    csv = get_google_csv(ticker, start_date, end_date, unique_search)
    data = parse_csv(csv)
    for d in data:
        date, price = d
        print(date.strftime("%m/%d/%Y"), price)

if __name__ == "__main__":
    parser=optparse.OptionParser()    
    parser.add_option("-t", "--ticker", dest="ticker", default="GOOG", help="ticker name; eg. AAPL, GOOG")
    parser.add_option("-s", "--start", dest="start_date", default="01,01,2000", help="start date, format is MM,DD,YYYY")
    parser.add_option("-e", "--end", dest="end_date", default="01,01,2010", help="end date, format is MM,DD,YYYY")
    parser.add_option("-x", "--search", dest="unique_search", default=None, help="explicit search term for Google, eg. \"INDEXDJX:.DJI\", ignores ticker")
    
    (options, args) = parser.parse_args()
    script(options.ticker, options.start_date, options.end_date, options.unique_search)
    
    

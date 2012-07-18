#$Id: optz.py 1 2011-07-11 20:41:57Z svilen_dobrev $
# -*- coding: utf-8 -*-

if 0:   #very simple independent ones, copy-paste from here
    #booleans/count only:
    def opt( *xx):
        n=0
        for x in xx:
            while x in sys.argv: n +=1; sys.argv.remove( x )
        return n

    #booleans only:
    def opt( *xx):
        for x in xx:
            if x in sys.argv: return sys.argv.remove( x ) or True
        return None
    o_n = opt('-n', '--dryrun')

    #booleans only:
    def opt(x):
        try: sys.argv.remove( x ); return True
        except ValueError: return None
    o_v = opt('-v') or opt('--verbose')

    # optparse simplifier/template
    import optparse
    oparser = optparse.OptionParser(
    '...')
    def optany( name, *short, **k):
        return oparser.add_option( dest=name, *(list(short)+['--'+name.replace('_','-')] ), **k)
    def optbool( name, *short, **k):
        return optany( name, action='store_true', *short, **k)
    optbool( 'verbose', '-v')
    optany(  'outfile', '-o', help= 'outfile, "-" for stdout')
    optany(  'maxsize', '-l', type=int, help= 'max size in MBs')
    options,args = oparser.parse_args()


#more complex:  #TODO: argparse, positional, ArgumentDefaultsHelpFormatter
import optparse, sys
def make( *a,**k):
    global oparser
    oparser = optparse.OptionParser( *a,**k)
make()
def usage( u):
    oparser.set_usage( u)
def optany( name, *short, **k):
    parser = k.pop( 'oparser', oparser)
    if sys.version_info[0]<3:
        h = k.pop( 'help', None)
        if h is not None:
            k['help'] = isinstance( h, unicode) and h or h.decode( 'utf8')
    return parser.add_option( dest=name, *(list(short)+['--'+name.replace('_','-')] ), **k)
def optbool( name, *short, **k):
    return optany( name, action='store_true', *short, **k)
_int = int
def optint( name, *short, **k):
    return optany( name, type=_int, *short, **k)
addopt = optany
addopt1 = addbool = optbool

def optappend( name, *short, **k):
    return optany( name, action='append', *short, **k)
def optcount( name, *short, **k):
    return optany( name, action='count', default=0, *short, **k)

def getoptz():
    options,args = oparser.parse_args()
    return options,args

add = any = str = text = addopt
add1= bool = addbool
int = optint
append = optappend
count  = optcount
get = parse = getoptz
help = usage

def group( name, **k):
    g = oparser.add_option_group( optparse.OptionGroup( oparser, name, **k))
    if not hasattr(oparser, 'options_dict'): oparser.options_dict = {}
    oparser.options_dict[ name] = g
    return g
def grouparg( name, **k):
    return dict( oparser= group( name, **k))

if 0:
    import optz
    optz.bool( 'simvolni',  '-L',   help= 'обхожда и символни връзки')
    optz.text( 'prevodi',            help= 'речник с преводи')
    optz.append( 'etiket',   '-e',  help= 'добавя етикета към _всички описи')
    optz.count( 'podrobno',  '-v',  help= 'показва подробности', default=0)

# vim:ts=4:sw=4:expandtab

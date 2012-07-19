# -*- coding: utf-8 -*-
#for p in sorted( set(re.findall( "'\w+'", file( '/home/az/pygrammar').read()))): print p[1:-1]

translation_constants = '''
False       Не Лъжа
None        Нищо
True        Да Истина
'''

translation = translation_constants + '''
and         и
as          като
assert      осигури
break       спри
class       клас
continue    продължи
def         деф
del         изтрий
elif        инако
else        иначе
except      освен
finally     винаги задължително
for         за всяко всички
from        от
global      глобални
if          ако
import      внеси
in          във
is          е
lambda      ламбда
nonlocal    нелокални
not         не
or          или
pass        карай
raise       вдигни
return      върни
try         опитай
while       докато
with        със
yield       предай произведи добий
'''
extra_charset = 'А-Яа-я'


p2b = dict( a.strip().split()[:2]
            for a in translation.split('\n')
            if a.strip() )

import sys, re
from svd_util import optz
optz.bool( 'lat2cyr', default= False)
optz.bool( 'grammar', default= False)
optz.bool( 'vim',     default= False)
#optz.bool( 'all_variants',  default= False, help= 'allow all alternatives; default: only first listed')
optz.bool( 'dump', )
opts,args = optz.get()

def tx( w):
    w = p2b.get(w,w)
    if opts.lat2cyr:
        from util import lat2cyr
        w = lat2cyr.zvuchene.lat2cyr(w)
    return w


class reader:
    def __init__( me):
        me.pending = None
        for a in sys.stdin:
            a = a.rstrip()
            me.doer( a)


class grammar( reader):
    def doer( me, a):
        l = re.split( "('\w+')", a)
        if len(l) == 1: r = l
        else:
            #print( '#',l)
            r = []
            for i,w in enumerate( l):
                if w and i%2 ==1:
                    wt = p2b[ w[1:-1] ]
                    w = "( %(w)s | '%(wt)s' )" % locals()
                r.append(w)
        print( ''.join( r ))

class vim( reader):
    funchdr = 'syn match pythonFunction'
    @classmethod
    def vimfuncpat( me, t):
        # \ "\%(\%(def\s\|class\s\|@\)\s*\)\@<=\h\%(\w\|\.\)*" contained

        def replfunc( m):
            e = m.group(0)
            r = []
            for w in m.group(1).split('\\|'):
                r.append( w)
                i = w.split( '\\s', 1)[0]
                w = tx(i)
                if w != i: r.append( w+'\\s')
            return e[ :m.start(1)-m.start(0)] + '\\|'.join( r) + e[ m.end(1)-m.start(0): ]

        t = t.strip()
        if t.startswith( '\\ '): t = t[2:]
        t = t.replace( '\\w', '['+extra_charset+ 'A-Za-z_0-9]')
        t = t.replace( '\\h', '['+extra_charset+ 'A-Za-z_]')
        alt = re.sub( r'\((\w.*?)\\\)', replfunc, t)
        #l = re.split( '(\\.|\W)', t)
        print( 'syn clear pythonFunction')  #else duplicates
        print( me.funchdr, alt)

    def doer( me, a):
        if a.strip() and me.pending:
            me.pending( a)
            me.pending = None
            return

        l = re.split( '[\s,]+', a)
        if l[:2] == 'syn keyword'.split() and l[2] in '''
            pythonStatement
            pythonStatement
            pythonStatement
            pythonStatement
            pythonConditional
            pythonRepeat
            pythonOperator
            pythonException
            pythonInclude
            '''.split():

            r = [tx(w) for w in l[3:]]
            print( ' '.join( l[:3] + r ))
            return

        if l[:3] == me.funchdr.split():
            r = l[3:]
            if r: me.vimfuncpat( a.split( 'pythonFunction')[-1] )
            else: me.pending = me.vimfuncpat

class plain( reader):
    def doer( me, a):
        l = re.split( '(\W+)', a)
        r = [tx(w) for w in l]
        print( ''.join( r ))

if opts.dump:
    print( '\n'.join( k+':\t '+v for k,v in sorted( p2b.items())))
else:
    if opts.grammar: doer = grammar
    elif opts.vim:  doer = vim
    else: doer = plain
    doer()

#for x in 'Нищо Да Не'.split(): print( ', '.join( str(ord(y)) for y in x), '//', x)

methods = dict(
    builtin = '''
        abs         абс
        all         всички
        any         коедае
        ascii       текстпрост
        bin         двоично
        callable    изпълним
        chr         символно
        compile     компилирай
        delattr     изтрийатр
        dir         съдържание
        divmod      остмод
        eval        изчисли
        exec        изпълни
        format      оформи
        getattr     дайатр
        globals     глобални
        hasattr     имаатр
        hash        хеш
        hex         ш16чно
        id          ид
        input       въведи
        isinstance  еекземпляр
        issubclass  еподклас
        iter        итер
        len         бр
        locals      локални
        max         макс
        min         мин
        next        следващ
        oct         осмично
        ord         поредно
        pow         степен
        print       печат печатай
        repr        текстпълен
        round       закръгли
        setattr     сложиатр
        sorted      подредени
        sum         сума
        vars        променливи
        ''',

    builtin_types = translation_constants + '''
        Ellipsis        Многоточие
        NotImplemented  НеНаправено
        bool            булево
        memoryview      памет
        bytearray       байтовмасив
        bytes           байтове
        classmethod     класовметод
        complex         комплексно
        dict            речник
        enumerate       изброени
        filter          филтър
        float           плаващочисло
        frozenset       множество
        property        свойство
        int             цялочисло
        list            списък
        map             съответствие
        object          обект
        range           поредни
        reversed        наобратно обърнати преобърнати
        set             множество множ
        slice           резен
        staticmethod    статиченметод
        str             текст низ стр стринг
        super           свръх
        tuple           двойка
        type            тип
        zip             цип зип
        ''',

    dict= '''
        get         дай
        setdefault  сложиаконяма
        pop         извади изкарай
        popitem     извадидвойка
        keys        ключове
        items       двойки
        values      стойности
        update      обнови
        fromkeys    сключове
        clear       изчисти
        copy        копирай
        ''',

    list= '''
        append      допълни
        insert      вмъкни
        extend      разшири удължи
        pop         извади изкарай
        remove      изтрий
        index       намери
        count       брой
        reverse     обърниреда
        sort        подреди
        ''',

    set= '''
        add             добави
        clear           изчисти
        copy            копирай
        discard         махни
        difference                  разлика
        difference_update           обнови_като_разлика
        intersection                сечение
        intersection_update         обнови_като_сечение
        isdisjoint      непресича
        issubset        еподмножество
        issuperset      енадмножество
        pop             извади изкарай
        remove          изтрий
        symmetric_difference        двупосочна_разлика      двойна_разлика
        symmetric_difference_update обнови_като_двупосочна_разлика обнови_като_двойна_разлика
        union           обединение
        update          обнови
        ''',
    str= '''
        encode          кодирай
        replace         замести
        split           раздели
        rsplit          драздели раздели_отзад раздели_открая
        join            слепи сглоби
        capitalize      заглавие
        title           заглавнидуми
        center          центрирай всредатаподравни подравни_среда
        count           брой
        expandtabs      разпънитаб
        find            търси
        rfind           дтърси      търси_отзад     търси–открая
        index           намери
        rindex          днамери     намери_отзад    намери_открая
        partition       разцепи
        rpartition      дразцепи    разцепи_отзад   разцепи_открая
        ljust           лподравни   лявоподравни    подравни_ляво
        rjust           дподравни   дясноподравни   подравни_дясно
        strip           почисти
        lstrip          лпочисти    почисти_отпред  почисти_отначало
        rstrip          дпочисти    почисти_отзад   почисти_открая
        splitlines      разделиредове
        translate       преведи
        swapcase        размени_големималки     размени_големималкибукви
        lower           малки       малкибукви
        upper           големи      големибукви
        startswith      започвас
        endswith        свършвас
        islower         емалка      емалкабуква
        isupper         еголяма     еголямабуква
        istitle         езаглавнидуми
        isspace         eмясто      еразредка   еинтервал
        isdecimal       едесетично
        isdigit         ецифра
        isnumeric       ечисло
        isalpha         ебуква
        isalnum         ебуквочисло
        isidentifier    еидентификатор  еиме
        isprintable     епечатаемо      етекст
        zfill           запълни0        запълнинули
        format          формат        оформи
        format_map      формат_речник оформи_речник
        maketrans       направи_превод
        ''',
)
# vim:ts=4:sw=4:expandtab

Welcome to smok
===============

Translated Python 3 clone: replacing english words (operators, names, funcs, messages - if,else,for,..) with another language (Bulgarian - ако,иначе,за). 
For kids and people to think and write in their own language, instead of suffer with the alternatives - near-"english", transliteration into latin, mixed latin-cyrilic.

Преведен Питон 3: замества английските думи (оператори, имена и съобщения - if,else,for,..) с друг език (Български - ако,иначе,за). 
За деца, и хора които искат да мислят и пишат на собствения си език - вместо да се мъчат с алтернативите - почти-"английски", български на латиница или смес от кирилица и латиница.


--------

this is attempt at translated python, into using bulgarian keywords - replacing the english (if,else,for,..).

 * why:
  * python3 allows any identifiers out of the box, but reading the mixed english-bulgarian result is.. nonsense.
   * i prefer to express my self in my language. and just then eventualy think of translation, if at all. and Nomen est omen. Even if i think correctly i may put the wrong english word. So it might be better to translate the code (identifiers+comments) properly after the concept is well expressed. And using english/latin alphabet for transliteraion is not good.
  * kids dont know english, nor the specific terms
 * what:
  * all reserved keywords
  * eventualy:
   * most builtin functions and types
   * the most used types' methods (like str.upper, list.append, dict.pop)
  * vim - syntax addition
 * how:
  * recompiles python 3, with appended grammar etc
  * both english and bulgarian (UTF8) wordings are usable
  * it's simple, other translations can be done (in other languages or charsets)


добре дошъл при смока 
=====================

това е опит за преведен питон, ползващ български думи (вместо if,else,for - напр. ако,иначе,за)

 * защо:
  * питон 3 поддържа имена на всякакви езици, но резултатната англо-българска смесица е.. безсмислена.
   * предпочитам да се изразявам на собствения си език. и чак после да мисля за превод, ако изобщо. а Имената са Всичко. Дори и да мисля правилно, може да сложа грешна чужда дума. Така че по-добре да се преведе кода (променливи + коментари) впоследствие, след като е вече измислен. А да се ползва английска/латинска азбука с транслитерация т.е. шльокавица, си е отврат.
  * децата не знаят английски, нито пък значението на термините
 * какво:
  * всички запазени думи (class, if, ...)
  * евентуално, имената на:
   * повечето вградени функции и типове
   * методите на най-ползваните типове (напр. str.upper, list.append, dict.pop)
  * vim: допълнителен оцветител на синтаксиса
 * как:
  * прекомпилира се питон 3, с допълнена граматика и пр.
  * достъпни са едновременно и българските (UTF8) и английските имена
  * схемата е проста, може да се направят и други преводи (към езици или кодови таблици)

```
клас Филминфо( Инфо):      #сега: почти преведено / now: almost translated
	@classmethod
	деф сглоби_име( кл, име ):
		имена = [ име ]
		ако   име.endswith('.bg'): имена.append( име[:-3])
		инако име.endswith('.ru'): имена.append( име[:-3])
		иначе:
			имена.append( име+'.bg')
			имена.append( име+'.ru')
		върни инфо.име_от_превод( *имена)


клас Филминфо( Инфо):      #TODO: изцяло преведено / fully translated
    @класметод
    деф сглоби_име( кл, име ):
        имена = [ име ]
        ако   име.завършва('.bg'): имена.допълни( име[:-3])
        инако име.завършва('.ru'): имена.допълни( име[:-3])
        иначе: имена.допълни( име)
        върни Инфо.сглоби_име( *имена)


class Filminfo( Info):     #изцяло на английски / fully in english
    @classmethod
    def make_name( kl, name):
        names = [ name]
        if name.endswith('.bg'): names.append( ime[:-3])
        elif name.endswith('.ru'): names.append( име[:-3])
        else: names.append( ime)
        return Info.make_name( *names)

```

: http://smok.sourceforge.net/

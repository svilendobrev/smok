#include <ctype.h>
#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>
#include <wctype.h>

wchar_t *
mbstowcs_alloc (const char *string)
{
    size_t size = strlen (string) + 1;
    wchar_t *buf = (wchar_t *)malloc (size * sizeof (wchar_t));

    size = mbstowcs (buf, string, size);
    if (size == (size_t) -1)
        return NULL;
    buf = (wchar_t *)realloc (buf, (size + 1) * sizeof (wchar_t));
    return buf;
}

int
main(int argc, char **argv)
{
    printf( "loca %s\n", setlocale( LC_ALL, "") );
    while (++argv,--argc) {
        wchar_t * b = mbstowcs_alloc( *argv) ;
         printf( "isa %s %d %d\n", *argv,
                 *b,
                 iswalpha(
                         *b
                        )
                 );
    }
}


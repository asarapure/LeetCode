__author__ = 'asarapure'


def remove_markup_html(s):
    tag = False
    quote = False
    out = ""

    for c in s :
        # assert not tag
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote :
            tag = False
        elif (c == '"' or c =="'") and tag :
            print(tag)
            # assert False
            quote = not quote
        elif tag is False :
            out = out + c
    return out


# print(remove_markup_html('<b>foo</b>'))
# print(remove_markup_html('<b>"foo"</b>'))
# print(remove_markup_html('"<b>foo</b>"'))
# print(remove_markup_html('<"b">foo</"b" >'))
print(remove_markup_html('"foo"'))

"""
Treating this problem as a finite state machine one. Depending on the state in which
one is, do a certain thing.
https://www.evernote.com/shard/s396/nl/73918192/d81faa8b-a20c-44e9-b1d0-1626e8aaac2f
"""
Comprehensive Python Cheatsheet
Download text file, Buy PDF, Fork me on GitHub or Check out FAQ.

Monty Python

Contents
    1. Collections:   List, Dictionary, Set, Tuple, Range, Enumerate, Iterator, Generator.
    2. Types:            Type, String, Regular_Exp, Format, Numbers, Combinatorics, Datetime.
    3. Syntax:           Args, Inline, Import, Decorator, Class, Duck_Types, Enum, Exception.
    4. System:          Exit, Print, Input, Command_Line_Arguments, Open, Path, OS_Commands.
    5. Data:               JSON, Pickle, CSV, SQLite, Bytes, Struct, Array, Memory_View, Deque.
    6. Advanced:     Threading, Operator, Introspection, Metaprograming, Eval, Coroutines.
    7. Libraries:        Progress_Bar, Plot, Table, Curses, Logging, Scraping, Web, Profile,
                                  NumPy, Image, Audio, Games, Data.

Main
if __name__ == '__main__':     # Runs main() if file wasn't imported.
    main()
List
<list> = <list>[<slice>]       # Or: <list>[from_inclusive : to_exclusive : ±step]
<list>.append(<el>)            # Or: <list> += [<el>]
<list>.extend(<collection>)    # Or: <list> += <collection>
<list>.sort()                  # Sorts in ascending order.
<list>.reverse()               # Reverses the list in-place.
<list> = sorted(<collection>)  # Returns a new sorted list.
<iter> = reversed(<list>)      # Returns reversed iterator.

Requirements
============

- python 2.7
- tremendous (installable with pip)

optional but recommanded:
  
- graphviz and the dot command
- evince (default) or another pdf reader 
  

Getting started
==================================

in ``./python-earley_parser/`` directory run ``make dot``


FAQ
===

Q: How to change the grammar ?
A: Currently there is no easy way to change the grammar, check out 
   `grammar_from_api@grammar.py` file to see current grammar.

Q: How does it works ?
A: The parser works in two step :
#. Build earley super set, after the sentence given in input, 
   see `parser@earley_parser`
   
   #. Complete, scan or do prediction on any generated item from ess.items list
      
   #. When you finished a) a.k.a you can't add any items, clean up the mess, 
         some items are usefull for the first step but won't be of any interrest for
         the second step.
      
#. Build parse trees based on cool item from `ess.items`, this step occurs, by now, 
      in `ParseRuleSet@parse_tools.py` and `buid_parse_tree@earley_parser.py`
   
#. Add semantic rules based on the parsed trees, be carful earley parser don't solve 
      ambiguity, so you might end up with several trees!

Q: How complex is the earley parser ?
A: Based on Earley's paper it's a $n^3$ algorithm...

Q: Which grammar can earley parser process ?
A: Every grammar ever ! At least that's what I understood.

Q: Where can I find out more about the earley algorithm ?
A: check out mendley's output @ http://www.mendeley.com/research-papers/search/#0/earley

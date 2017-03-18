Requirements
============

- python 2.7

optional but recommended:
  
- graphviz and the dot command
- evince (default) or another pdf reader 
  

Getting started
===============

in ``./earleyparser/`` directory run ``make dot`` or ``make flat``.


FAQ
===

Q: How to change the grammar ?  A: Currently there is no easy way to
change the grammar, check out `grammar::grammar_from_api` file to
see current grammar.

Q: How does it works ?  A: The parser works in two step :

#. Build earley super set, after the sentence given in input, 
   see `earley_parser::parser`
   
   #. Complete, scan or do prediction on any generated item from ess.items list
      
   #. When you finished a) a.k.a you can't add any items, clean up the
      mess, some items are usefull for the first step but won't be of
      any interrest for the second step.
      
#. Build parse trees based on cool item from `ess.items`, this step
   occurs, by now, in `parse_tools::ParseRuleSet` and
   `earley_parser::buid_parse_tree`
   
#. Add semantic rules based on the parsed trees, be carful earley parser don't solve 
   ambiguity, so you might end up with several trees!

Q: How complex is the earley parser ?  A: Based on Earley's paper it's
a $n^3$ algorithm...

Q: Which grammar can earley parser process ?  A: Every grammar ever !
At least that's what I understood.

Q: Where can I find out more about the earley algorithm ?

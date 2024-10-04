# special-functions
Special Functions in Python
     =========================================================
=>In Python programming, we have 3 Types of Special Functions. They are

			1. filter()
			2. map()
			3. reduce()

=========================================================
						1. filter()
=========================================================
=>filter() is used for  "Filtering out some elements from list of elements by applying to function".
=>Syntax:-        varname=filter(FunctionName, Iterable_object)

---------------------
Explanation:
---------------------
=>here 'varname' is an object of type <class,'filter'> and we can convert into any iteratable object by using type 
   casting functions.
=>"FunctionName" represents either Normal function or anonymous functions.
=>"Iterable_object" represents Sequence, List, set and dict types.
=>The execution process of filter() is that  " Each Value of Iterable object sends to Function Name. If the function return True then the element will be filtered. if the Function returns False then that element will be neglected/not filtered ". This process will be continued until all elements of Iterable object completed".

-----------------------------------------------------------------------------------------------------------------

====================================
				2) map()
====================================
=>map() is used for obtaining new Iterable object from existing iterable object by applying old iterable elements to the function.
=>In otherwords, map() is used for obtaining new list of elements  from  existing list of elements by applying old list  elements to the function.

=>Syntax:-      varname=map(FunctionName,Iterable_object)
				
=>here 'varname' is an object of type <class,map'> and we can convert into any iteratable object by using type casting functions.
=>"FunctionName" represents either Normal function or anonymous functions.
=>"Iterable_object" represents Sequence, List, set and dict types.
=>The execution process of map() is that " map() sends every element of iterable object to the specified function, process it and returns the modified value (result) and new list of elements will be obtained". This process will be continued until all elements of Iterable_object completed.

-----------------------------------------------------------------------------------------------------------------

================================
				3. reduce()
================================
=>reduce() is used for obtaining a single element / result from given iterable object by applying to a function.
=>Syntax:-
		varname=functools.reduce(function-name,iterable-object)
=>here varname is an object of int, float,bool,complex,str only
=>The reduce() belongs to a pre-defined module called " functools".

---------------------------------------
Internal Flow of reduce()
---------------------------------------
step-1:- Initially, reduce() selects  First Two values of Iterable object and place them in First var and Second var .
step-2:- The function-name(lambda or normal function) utilizes the values of First var and                     
             Second var and applied to the specified logic and obtains the result.
Step-3:- reduce () places the result of function-name in First variable and reduce() 
              selects the succeeding element of Iterable object and places in second variable.
Step-4: Repeat  Step-2 and Step-3 until all elements completed in		             
             Iterable object and returns the result of First Variable.
             
-----------------------------------------------------------------------------------------------------------------

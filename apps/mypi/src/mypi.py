
import sympy
import sys


#####################
#  GREGORY LEIBNIZ  #
#####################
# http://mathworld.wolfram.com/PiFormulas.html
def gregory_leibniz( k ) :
  if k < 1 :
    raise ValueError( "k must be >= 1." )
  series_exp = ""

  for i in range( 1, int(k)+1 ) :
    if i % 2 == 0 :
      term_numer = "-1"
    else :
      term_numer = "1"
    term_denom = "((2*" + str( i ) + ")-1)"
    series_exp += "+(" + term_numer + "/" + term_denom + ")"

  series_exp = "4*(" + series_exp[1:] + ")"
  print "Evaluating series expression:\n" + series_exp
  n = sympy.sympify( series_exp )
  print "\nresult:"
  return n.evalf()


#########################
#  THREAD OF EXECUTION  #
#########################
if __name__ == "__main__" :
  #method = get_method() # <--- implement this.
  #if method == "gregory_leibniz" :
  if True :
    print gregory_leibniz( sys.argv[1] )


#########
#  EOF  #
#########

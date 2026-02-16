# a function with one argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# default parameter value
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
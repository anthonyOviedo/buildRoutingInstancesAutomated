# buidRoutingInstancesAutomated
Short code to create those comands needed to set conections betwen rounting instances in a master router for junnos devices


MANUAL:

The file already has an Example with 3 instances  (A)_1________2__(B)__3________4_(C)

step 1:
to set A , B , C routers you have to wirte the name first followed by its interfaces:


A 1

B 2 3 

C 4


step 2:
save that in txt file named "routers.txt" file in the same path as the .py file.

step 3:
run the py srcipt

step 4:
copy the comands created in comandos.tx file in the same path as the .py file.



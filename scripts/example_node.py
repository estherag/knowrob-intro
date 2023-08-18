#!/usr/bin/env python

import roslib
import rospy
from knowrob_intro.prolog_query import PrologQuery

roslib.load_manifest('rosprolog')

# --------------- INITIALIZE node, quering class and database ----------------

rospy.init_node('example_query_owl')  # initialize node
pq = PrologQuery()  # create a prolog query class instance

# load example.owl in the knowrob database to access its content
query = pq.prolog_query(
    "load_owl('package://knowrob_intro/owl/krr_exercise.owl',\
     [namespace(pap, 'http://www.airlab.org/tiago/pick-and-place#')]).")

# --------------------------------------------------------------------------

# Quering examples

# (Find) all instances of milk
query = pq.prolog_query("instance_of(X, pap:'Milk').")
print("Instances of Milk:")
pq.get_all_solutions(query)

# (Find) all instances of Food
query = pq.prolog_query("instance_of(X, pap:'Food').")
print("Query result:")
print("Instances of Food:")
food_instances = pq.get_all_solutions(query)
print("First food instance found {}".format(food_instances[0]))

# (Find) all classes that are domain of has mass value property
query = pq.prolog_query("has_domain(soma:'hasMassValue',X).")
print("Individuals with mass value:")
pq.get_all_solutions(query)

# (Find) which individuals are mass attribute of milk product 1
query = pq.prolog_query("holds(pap:'milk1', soma:hasMassAttribute, X)")
print("Mass attribute of milk1:")
pq.get_all_solutions(query)
query = pq.prolog_query("holds(pap:weight_value_milk, soma:hasMassValue, X)")
print("Value of mass attribute of milk1:")
pq.get_all_solutions(query)

# (Find) all instances of Food
query = pq.prolog_query("instance_of(X, pap:'Food').")
print("Query result:")
print(query)
print("\nFormated solution\n")
s = pq.get_all_solutions(query)
print("Not formated solution")
print(s)
print("\nFirst element of solution")
print(s[0])

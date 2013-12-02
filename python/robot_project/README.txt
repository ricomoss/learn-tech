==========================
Pixolut Robot Project
==========================

Motivation
==================================

I received this UML test from Pixolut as a Python test for a possible contract position.  With their permission
I am adding the test and solution to my Learn Tech project.  The test is given as Java UML and provided an
excellent example of how to convert Java concepts to Python implementations.

Many thanks to Pixolut for allowing me to include this.
    
pixolut_exam.pdf
==================================

The test definition.  You'll notice a brief setup of the test, including instructions for setup.  You'll notice
it's catered to Visual Studios, but any IDE/editor would be sufficient.  I used PyCharm.

My Implementation
==================================

1. robot.py
    Implementation of the robot defined in the UML.  I took a few liberties since Java code can't be mapped
    completely.  Notice the lack of the Move and Heading classes.  I decided to approach it with a random
    heading given in terms of degrees from North (0 degrees).  The 'North', 'South', 'East', 'West' versions
    of heading were abandoned to provide a more meaningful approach to orientation.
    
    One could implement a "Compass" utility the robot could inherit.  I would provide a method "get_heading"
    which would map an orientation in degrees into 'N', 'NE', 'E', etc.


2. motor.py
    Implementation of the motors defined in the UML.  Due to the vague description of the mechanisms
    surrounding the motors I decided to keep them very simple.  In one instance I substitute "ROTATIONS_PER_MOVE"
    in place of "self.wheel_rotations".  I'm not sure if it's a typo, but it seemed odd to me that the distance
    per rotation would vary based on the number of rotations.  This would make sense if the diameter of the
    wheel was varied, but it would have to significantly change to provide this much variance.

3. tests.py
    As per the instructions I provided a complete set of unit tests for the robot and motors.  Once could easily
    implement integration tests by providing tests that instantiate a robot and test the interface to all the
    inherited objects. (robot.motor.get_total_distance())

from plone.app.testing import ROBOT_TEST_LEVEL
from plone.testing import layered
from ploneintranet.suite.testing import PLONEINTRANET_SUITE_ROBOT

import os
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.level = ROBOT_TEST_LEVEL
    current_dir = os.path.abspath(os.path.dirname(__file__))
    robot_dir = os.path.join(current_dir, 'robot')
    robot_tests = [
        os.path.join('robot', doc) for doc in
        os.listdir(robot_dir) if doc.endswith('.robot') and
        doc.startswith('test_')
    ]
    for robot_test in robot_tests:
        robottestsuite = robotsuite.RobotTestSuite(robot_test)
        suite.addTests([
            layered(
                robottestsuite,
                layer=PLONEINTRANET_SUITE_ROBOT
            ),
        ])
    return suite

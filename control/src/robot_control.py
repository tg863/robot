#!/usr/bin/env python

from udm_project_control.srv import *
import rospy
import time
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list



class groupService:

	def __init__(self):
		rospy.init_node('udm_project_commander')
		moveit_commander.roscpp_initialize(sys.argv)

		self.robot=moveit_commander.RobotCommander()
		self.scene =moveit_commander.PlanningSceneInterface()
		self.legmr =moveit_commander.MoveGroupCommander("legmr")
		self.legml =moveit_commander.MoveGroupCommander("legml")
		self.legfr =moveit_commander.MoveGroupCommander("legfr")
		self.legfl =moveit_commander.MoveGroupCommander("legfl")
		rospy.Service('control', control, self.handle_req)
		rospy.spin()


	def handle_req(self,req):
		try:
			print req
			command = req.mouvement
			self.legmr.set_named_target("startmr")
			self.legml.set_named_target("startml")
			self.legfr.set_named_target("startfr")
			self.legfl.set_named_target("startfl")
			count=0

			if(command.data == "front"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.legmr.set_named_target("frontmr")
					self.legfr.set_named_target("startfr")
					plan1a=self.legmr.plan()
					time.sleep(1)
					self.legfl.set_named_target("frontfl")
					self.legml.set_named_target("startml")
					plan2a=self.legfl.plan()
					time.sleep(1)
					self.legfr.set_named_target("frontfr")
					self.legmr.set_named_target("startmr")
					plan3a=self.legfr.plan()
					time.sleep(1)
					self.legml.set_named_target("frontml")
					self.legfl.set_named_target("startfl")
					plan4a=self.legml.plan()
					time.sleep(1)
					count+=1
				count=0
				rep=controlResponse()
				rep.res.data=True
				rep.message.data="Success"

			elif(command.data == "back"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.legmr.set_named_target("backmr")
					self.legfr.set_named_target("startfr")
					plan1a=self.legmr.plan()
					time.sleep(0.8)
					self.legfl.set_named_target("backfl")
					self.legml.set_named_target("startml")
					plan2a=self.legfl.plan()
					time.sleep(0.8)
					self.legfr.set_named_target("backfr")
					self.legmr.set_named_target("startmr")
					plan3a=self.legfr.plan()
					time.sleep(0.8)
					self.legml.set_named_target("backml")
					self.legfl.set_named_target("startfl")
					plan4a=self.legml.plan()
					time.sleep(0.8)
					count+=1
				count=0
				rep=controlResponse()
				rep.res.data=True
				rep.message.data="Success"

			elif(command.data == "right"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.legmr.set_named_target("rightmr")
					self.legfr.set_named_target("startrightfr")
					plan1a=self.legmr.plan()
					time.sleep(0.8)
					self.legfl.set_named_target("rightfl")
					self.legml.set_named_target("startrightml")
					plan2a=self.legfl.plan()
					time.sleep(0.8)
					self.legfr.set_named_target("rightfr")
					self.legmr.set_named_target("startrightmr")
					plan3a=self.legfr.plan()
					time.sleep(0.8)
					self.legml.set_named_target("rightml")
					self.legfl.set_named_target("startrightfl")
					plan4a=self.legml.plan()
					time.sleep(0.8)
					count+=1
				count=0
				rep=controlResponse()
				rep.res.data=True
				rep.message.data="Success"

			elif(command.data == "left"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.legmr.set_named_target("leftmr")
					self.legfr.set_named_target("startrightfr")
					plan1a=self.legmr.plan()
					time.sleep(0.8)
					self.legfl.set_named_target("leftfl")
					self.legml.set_named_target("startrightml")
					plan2a=self.legfl.plan()
					time.sleep(0.8)
					self.legfr.set_named_target("leftfr")
					self.legmr.set_named_target("startrightmr")
					plan3a=self.legfr.plan()
					time.sleep(0.8)
					self.legml.set_named_target("leftml")
					self.legfl.set_named_target("startrightfl")
					plan4a=self.legml.plan()
					time.sleep(0.8)
					count+=1
				count=0
				rep=controlResponse()
				rep.res.data=True
				rep.message.data="Success"
			return rep
		except Exception as e:
			rep=controlResponse()
			print e
			return rep

if __name__ == "__main__":
	groupService()

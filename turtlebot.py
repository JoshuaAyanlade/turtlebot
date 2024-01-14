from robot_control_class import RobotControl
    
class RobControl:
    def __init__(self):
        self.turtlebot = RobotControl()
        self.right_laser_value=0
        self.left_laser_value=0
        self.front_laser_value=0
        self.laser_left =0
        self.laser_right=0
        self.safe_distance=1
        self.turn_speed = 0.3
        self.turn_time = 5
        self.turn_direction = "clockwise"
        self.move = True
    
    def init_position(self):
        self.front_laser_value = self.turtlebot.get_laser(360)
        while(self.front_laser_value>self.safe_distance):
            self.turtlebot.move_straight()
            self.front_laser_value = self.turtlebot.get_laser(360)
        self.turtlebot.stop_robot()
        self.turtlebot.turn(self.turn_direction, self.turn_speed, self.turn_time) 

    def get_laser_readings(self):
        self.right_laser_value = self.turtlebot.get_laser(0)
        self.left_laser_value = self.turtlebot.get_laser(719)
        return self.left_laser_value,self.right_laser_value
    
    def main(self):
        self.init_position()
        while(self.move):
            self.laser_left,self.laser_right = self.get_laser_readings()
            self.turtlebot.move_straight()
            if (self.laser_left == float('inf') or self.laser_right == float('inf')):
                self.move = False
        self.turtlebot.stop_robot()

if __name__ == '__main__':
    
    rosbot = RobControl()
    try:
        rosbot.main()

    except rospy.ROSInterruptException:
        pass


form launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([



        launch_ros.action.Node(
            namespace="turtlesim1",package='turtlesim', executable='turltesim_node',output='screen'),
            launch_ros.action.Node(
                namespace= "turltesim" , package 'turtlesim', executable='turtle_teleop_key',output ='teleop '),



            )
        )
    ]
    )